from course.models import Category


def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    sub_categories = Category.objects.filter(parent__isnull=False)

    context = {
        'categories': categories,
        "sub_categories": sub_categories
    }
    return context
