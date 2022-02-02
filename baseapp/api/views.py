from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from baseapp.models import Course, Lecture
from .serializers import CourseSerializer, LectureSerializer

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
    pass

@api_view(["GET"])
def getParticularLecture(request, slug):
    pass