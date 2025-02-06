from django.db import models
from course.models import Course, Chapter, Lesson, UserCourse
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Competition(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='competition/%Y/%m/%d/')
    long_image = models.ImageField(upload_to='competition/%Y/%m/%d/', blank=True, null=True)
    video = models.FileField(upload_to='videos/competition/%Y/%m/%d/', blank=True, null=True)
    max_join = models.IntegerField(default=30)
    joined = models.ManyToManyField(User, related_name='competition_joined')
    entry_fee = models.FloatField(default=0)
    prize = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    features = models.SlugField(max_length=200)
    is_featured = models.BooleanField(default=False)
    keywords = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    canceled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    lession = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField()
    image = models.ImageField(upload_to='question/%Y/%m/%d/')
    mark = models.IntegerField(default=10)
    pass_mark = models.IntegerField(default=3)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    answer = models.TextField()
    image = models.ImageField(upload_to='question/%Y/%m/%d/')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    image = models.ImageField(upload_to='answer/%Y/%m/%d/')
    mark = models.IntegerField(default=0)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


















