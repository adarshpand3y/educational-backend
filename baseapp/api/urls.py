from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('', views.getRoutes),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', views.createUser),
    path('setuserdetails/', views.setUserDetails),

    path('getallcourses/', views.getAllCourses),
    path('getalllectures/', views.getAllLectures),
    path('course/<str:slug>', views.getParticularCourse),
    path('getcourselectures/<str:slug>', views.getAllLecturesOfCourse),
    path('lecture/<str:slug>', views.getParticularLecture),

    path('blogs/<int:pageNum>', views.blogs),
    path('blog/<str:slug>', views.blogpost),
]