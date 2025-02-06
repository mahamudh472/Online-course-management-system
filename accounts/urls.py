from django.urls import path
from .import views

app_name = "account"

urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name="register"),
    path('logout/', views.logoutView, name="logout"),
    path('profile/', views.profileView, name="profile"),
    path('profile/<str:username>', views.profileView, name="user_profile"),
]
