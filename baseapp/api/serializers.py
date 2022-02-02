from rest_framework import serializers

from baseapp.models import Course, Lecture

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'name', 'description', 'youtube_url']