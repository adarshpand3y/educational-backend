from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from baseapp.models import Course, Lecture, BlogPost
from django.core.paginator import Paginator, EmptyPage
from .serializers import BlogPostSerializer, CourseSerializer, LectureSerializer
from .validators import *

from django.contrib.auth.models import User
from baseapp.models import UserDetails

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

@api_view(["POST"])
def createUser(request):
    firstname = request.data.get("firstname", "")
    lastname = request.data.get("lastname", "")
    username = request.data.get("username", "")
    email = request.data.get("email", "")
    password = request.data.get("password", "")
    conf_password = request.data.get("conf_password", "")

    add1 = request.data.get("add1", "")
    add2 = request.data.get("add2", "")
    city = request.data.get("city", "")
    state = request.data.get("state", "")
    pincode = request.data.get("pincode", "")
    landmark = request.data.get("landmark", "")

    # check for errorneous input
    # TODO: use better way, is this robust enough ?
    # TODO: test all validation logics thoroughly, before production

    errors = {}
    errors["username"] = checkUname(uname=username)
    errors["firstname"] = checkFirstname(firstname=firstname)
    errors["lastname"] = checkLastname(lastname=lastname)
    errors["password"] = checkPassword(
        password=password,
        username=username,
        firstname=firstname,
        lastname=lastname,
        email=email,
    )
    errors["conf_password"] = checkConfPassword(
        password=password, confPassword=conf_password
    )
    errors["email"] = checkEmail(email)

    if (
        (not add1)
        or (not add2)
        or (not city)
        or (not state)
        or (not pincode)
        or (not landmark)
    ):
        errors[
            "userdetails"
        ] = "All of the adresses, city, state, pincode and landmark fields are required."

    # remove field(s), which has empty no error
    errors = {k: v for (k, v) in errors.items() if v}

    if len(errors) > 0:
        return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)

    # if len(firstname) < 3:
    #     return Response({"error": {"firstname": "First Name is too short"}}, status=status.HTTP_400_BAD_REQUEST)
    # if len(firstname) > 15:
    #     return Response({"error": {"fristname": "First Name is too big"}}, status=status.HTTP_400_BAD_REQUEST)
    # if len(lastname) < 3:
    #     return Response({"error": {"lastname": "Last Name is too short."}}, status=status.HTTP_400_BAD_REQUEST)
    # if len(lastname) > 15:
    #     return Response({"error": {"lastname": "Last Name is too big."}}, status=status.HTTP_400_BAD_REQUEST)
    # if len(username) < 8:
    #     return Response({"error": {"username": "Username is too short. Minimum 8 characters."}}, status=status.HTTP_400_BAD_REQUEST)
    # if len(username) > 15:
    #     return Response({"error": {"username": "Username is too big. Maximum 15 characters."}}, status=status.HTTP_400_BAD_REQUEST)
    # if password != conf_password:
    #     return Response({"error": {"confPassword": "Passwords do not match."}}, status=status.HTTP_400_BAD_REQUEST)
    # if User.objects.filter(username=username).exists():
    #     return Response({"error": {"username": "A user with that username already exists."}}, status=status.HTTP_400_BAD_REQUEST)
    # if User.objects.filter(email=email).exists():
    #     return Response({"error": {"email": "A user with that email already exists."}}, status=status.HTTP_400_BAD_REQUEST)

    # Create the user
    myuser = User.objects.create(
        username=username,
        email=email,
        password=password,
        first_name=firstname,
        last_name=lastname,
    )

    details = UserDetails.objects.create(
        user=myuser,
        # TODO: unused field
        number=1234,
        address1=add1,
        address2=add2,
        city=city,
        state=state,
        pincode=pincode,
        landmark=landmark,
    )

    return Response({"success": "User created, details saved successfully."})
    return Response(
        {"success": "User created, details saved successfully.", "userDetails": details}
    )

# unused function...
# @api_view(["POST"])
# def setUserDetails(request):
#     username = request.data.username
#     add1 = request.data.add1
#     add2 = request.data.add2
#     city = request.data.city
#     state = request.data.state
#     pincode = request.data.pincode
#     landmark = request.data.landmark

#     myuser = User.objects.get(username=username)

#     print(add1, add2, city, state, pincode, landmark)
#     details = UserDetails(
#         user=myuser,
#         address1=add1,
#         address2=add2,
#         city=city,
#         state=state,
#         pincode=pincode,
#         landmark=landmark
#     )
#     details.save()
#     return Response({"success": "Details saved successfully."})

@api_view(["GET"])
def getAllLectures(request):
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getAllCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getParticularCourse(request, slug):
    course = Course.objects.get(slug=slug)
    serializer = CourseSerializer(course)
    return Response(serializer.data)

@api_view(["GET"])
def getAllLecturesOfCourse(request, slug):
    course = Course.objects.get(slug=slug)
    lectures = Lecture.objects.filter(course=course)
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getParticularLecture(request, slug):
    lecture = Lecture.objects.get(slug=slug)
    course = CourseSerializer(lecture.course)
    serializedLecture = LectureSerializer(lecture)
    lectures = Lecture.objects.filter(course=lecture.course).order_by('course_index')
    serializedLectureList = LectureSerializer(lectures, many=True)
    responseDictionary = {"lectureData": serializedLecture.data, "lectureList": serializedLectureList.data, "course": course.data}
    return Response(responseDictionary)

@api_view(["GET"])
def blogs(request, pageNum):
    blogs = BlogPost.objects.exclude(privacy="PRIVATE").order_by("-publish_date")
    p = Paginator(blogs, 5) # Change this 1 to the required number of blogs per page in produciton
    try:
        blogs = p.page(pageNum)
    except EmptyPage:
        blogs = p.page(1)
    serializer = BlogPostSerializer(blogs, many=True)
    totalNumberOfPages = p.num_pages
    responseDict = {"blogs": serializer.data, "totalNumberOfPages": totalNumberOfPages}
    return Response(responseDict)

@api_view(["GET"])
def blogpost(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
    except:
        return Response({"error": "Blog Not Found."}, status=status.HTTP_404_NOT_FOUND)
    if blog.privacy == "PUBLIC":
        blog.views += 1
        blog.save()
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)
    else:
        return Response({"error": "Blog Not Found."}, status=status.HTTP_404_NOT_FOUND)
    