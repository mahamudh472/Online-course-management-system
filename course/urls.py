from django.urls import path
from .import views

app_name = "course"

urlpatterns = [
    path("details/<str:slug>", views.details, name="details"),
]
