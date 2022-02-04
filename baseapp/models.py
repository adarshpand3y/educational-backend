from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    one_line_description = models.CharField(max_length=300, blank=True, default="", help_text=('Describe the course in one but unforgettable line. Max 300 characters'))
    description = models.TextField(unique=True)
    image_url = models.CharField(max_length=200, default="", help_text=('Enter Image URL within 200 characters.'))
    high_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    @property
    def short_name(self):
        return truncatechars(self.name, 50)
    
    @property
    def short_description(self):
        return truncatechars(self.one_line_description, 50)

    def __str__(self):
        return truncatechars(self.name, 50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

class Lecture(models.Model):
    name = models.CharField(max_length=100, unique=True)
    one_line_description = models.CharField(max_length=300, blank=True, default="", help_text=('Describe the lecture in one but unforgettable line. Max 300 characters'))
    description = models.TextField(unique=True)
    youtube_url = models.CharField(max_length=100, unique=True)
    course_index = models.IntegerField(unique=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, unique=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    @property
    def short_name(self):
        return truncatechars(self.name, 50)
    
    @property
    def short_course(self):
        return truncatechars(self.course, 50)

    def __str__(self):
        return truncatechars(self.name, 50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lecture, self).save(*args, **kwargs)