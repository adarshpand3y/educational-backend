from rest_framework import serializers

from baseapp.models import Course, Lecture, BlogPost

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'one_line_description', 'description', 'image_url', 'high_price', 'price', 'slug']

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'name', 'one_line_description', 'description', 'youtube_url', 'course_index', 'slug']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title','description', 'body', 'views', 'publish_date', 'last_updated', 'slug']
