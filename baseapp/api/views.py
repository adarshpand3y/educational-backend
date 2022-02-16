from itertools import product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from baseapp.models import Course, Lecture, BlogPost, Product
from django.core.paginator import Paginator, EmptyPage
from .serializers import BlogPostSerializer, CourseSerializer, LectureSerializer, ProductSerializer

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
    firstname = request.data.firstname
    lastname = request.data.lastname
    username = request.data.username
    email = request.data.email
    password = request.data.password
    conf_password = request.data.conf_password

    # check for errorneous input
    if len(firstname) < 3:
        return Response({"error": "First Name is too short"}, status=status.HTTP_400_BAD_REQUEST)
    if len(firstname) > 15:
        return Response({"error": "First Name is too big"}, status=status.HTTP_400_BAD_REQUEST)
    if len(lastname) < 3:
        return Response({"error": "Last Name is too short."}, status=status.HTTP_400_BAD_REQUEST)
    if len(lastname) > 15:
        return Response({"error": "Last Name is too big."}, status=status.HTTP_400_BAD_REQUEST)
    if len(username) < 8:
        return Response({"error": "Username is too short. Minimum 8 characters."}, status=status.HTTP_400_BAD_REQUEST)
    if len(username) > 15:
        return Response({"error": "Username is too big. Maximum 15 characters."}, status=status.HTTP_400_BAD_REQUEST)
    if password != conf_password:
        return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({"error": "A user with that username already exists."}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({"error": "A user with that email already exists."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create the user
    myuser = User.objects.create_user(username, email, password)
    myuser.first_name = firstname
    myuser.last_name = lastname
    myuser.save()
    return Response({"success": "User created successfully."})

@api_view(["POST"])
def setUserDetails(request):
    username = request.data.username
    add1 = request.data.add1
    add2 = request.data.add2
    city = request.data.city
    state = request.data.state
    pincode = request.data.pincode
    landmark = request.data.landmark

    myuser = User.objects.get(username=username)

    print(add1, add2, city, state, pincode, landmark)
    details = UserDetails(
        user=myuser,
        address1=add1,
        address2=add2,
        city=city,
        state=state,
        pincode=pincode,
        landmark=landmark
    )
    details.save()
    return Response({"success": "Details saved successfully."})

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

@api_view(["GET"])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(["GET"])
def getcheckoutdetails(request, typeOfProduct, slug):
    print(typeOfProduct, slug)
    if typeOfProduct == "product":
        try:
            product = Product.objects.get(slug=slug)
        except:
            return Response({"error":"No such product found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif typeOfProduct == "course":
        try:
            course = Course.objects.get(slug=slug)
        except:
            return Response({"error":"No such course found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    return Response({"error":"No such item found!"}, status=status.HTTP_400_BAD_REQUEST)