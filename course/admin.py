from django.contrib import admin
from django.utils.html import format_html

from .models import Course, Chapter, Lesson, Category
from django.urls import reverse
from django.utils.http import urlencode


# Register your models here.

class LessionInline(admin.StackedInline):
    model = Lesson
    extra = 1


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ["name", 'category', 'duration', 'price', 'view_chapters']

    def view_chapters(self, obj):
        count = obj.chapter_set.count()
        url = (
                reverse("admin:course_chapter_changelist")
                + "?"
                + urlencode({"course__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Chapters</a>', url, count)

    view_chapters.short_description = "Chapters"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [LessionInline]
    list_display = ['name', 'course_link']
    list_filter = ['course__name']
    search_fields = ['name']

    def course_link(self, obj):
        url = (
                reverse("admin:course_chapter_changelist")
                + "?"
                + urlencode({"course__id": f"{obj.course.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.course.name)


class CategoryTypeFilter(admin.SimpleListFilter):
    title = 'Category Type'  # or use _('Category Type') for translated title
    parameter_name = 'cat_type'

    def lookups(self, request, model_admin):
        return (
            ('parent', 'Parent'),
            ('sub_category', 'Sub Category'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'parent':
            return queryset.filter(parent__isnull=True)
        if self.value() == 'sub_category':
            return queryset.filter(parent__isnull=False)
        return queryset

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'cat_type']
    list_filter = [CategoryTypeFilter]

    def cat_type(self, obj):
        if obj.parent:
            return "Sub Category"
        else:
            return "Parent"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
