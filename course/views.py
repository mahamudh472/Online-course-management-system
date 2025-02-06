from django.shortcuts import render
from .models import Course


def details(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        'course': course,
    }
    return render(request, "course/details.html", context)
