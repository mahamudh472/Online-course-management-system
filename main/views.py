from django.db.models import Q
from django.shortcuts import render
from course.models import Course, Category


# Create your views here.

def home(request):
    course_list = Course.objects.all()
    categories = Category.objects.all()
    context = {
        'course_list': course_list,
    }
    return render(request, "main/home.html", context)


def search(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get('category', '').strip()
    sub_category = request.GET.get('sub_category', '').strip()
    course_list = Course.objects.filter(
        Q(name__icontains=query) |
        Q(slug__icontains=query) |
        Q(keywords__icontains=query)
    )
    if not query:
        course_list = Course.objects.all()
    if category:
        course_list = course_list.filter(category__parent__name=category)
    if sub_category:
        course_list = course_list.filter(category__name=sub_category)

    course_list = course_list.distinct()
    context = {
        "course_list": course_list,
        "query": query,
        "cat": category,
        "sub_cat": sub_category
    }

    return render(request, "main/search.html", context)
