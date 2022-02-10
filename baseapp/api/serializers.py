from rest_framework import serializers

from baseapp.models import Course, Lecture

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'one_line_description', 'description', 'image_url', 'high_price', 'price', 'slug']

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'name', 'description', 'youtube_url']