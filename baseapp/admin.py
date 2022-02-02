from django.contrib import admin
from .models import Course, Lecture

class CourseAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'short_description')

class LectureAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'short_course', 'course_index')

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)