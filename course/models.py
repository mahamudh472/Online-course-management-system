from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='category_image/%Y/%m/%d/', blank=True, null=True)
    keywords = models.CharField(max_length=100)
    popularity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='course/%Y/%m/%d/')
    long_image = models.ImageField(upload_to='course/%Y/%m/%d/', blank=True, null=True)
    video = models.FileField(upload_to='videos/course/%Y/%m/%d/', blank=True, null=True)
    price = models.CharField(max_length=20)
    total_enrolled = models.IntegerField(default=0)
    duration = models.CharField(max_length=20)
    features = models.SlugField(max_length=200)
    is_featured = models.BooleanField(default=False)
    keywords = models.CharField(max_length=100)
    popularity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    video = models.FileField(upload_to='videos/lession/%Y/%m/%d/', blank=True, null=True)
    resource = models.FileField(upload_to='files/lession/%Y/%m/%d/', blank=True, null=True)
    duration = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    payment_info = models.TextField()
    is_complete = models.BooleanField(default=False)
    in_competition = models.BooleanField(default=False)
    completed_chapters = models.ManyToManyField(Chapter, related_name="completed_chapters")
    completed_lessons = models.ManyToManyField(Lesson, related_name="completed_lessons")
    mark = models.IntegerField(default=0)
    bonus_mark = models.IntegerField(default=0)
    show_in_profile = models.BooleanField(default=True)
    position = models.IntegerField(default=0)
    show_position_in_profile = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
