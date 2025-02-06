from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from accounts.models import Profile
from django.contrib.auth.models import User


# Create your views here.


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main:home')
        else:
            messages.error(request, "Wrong candidate")
    return render(request, "main/login.html")


def registerView(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        username = email.split("@")[0]
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                try:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        username=username
                    )
                    if user:
                        full_name = first_name + " " + last_name
                        profile = Profile.objects.create(
                            user=user,
                            full_name=full_name,

                        )
                        profile.save()
                        user = authenticate(username=username, password=password)
                        login(request, user)
                        return redirect('main:home')


                except:
                    messages.error(request, "Error creating account. please try again")
                    return redirect('account:register')

        else:
            messages.error(request, "Password and confirm password must be same")
            return redirect("account:register")
    return render(request, "main/register.html")


def logoutView(request):
    logout(request)
    return redirect("account:login")


def profileView(request, username=None):
    if username:
        profile = Profile.objects.get(user__username=username)
    else:
        profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }

    return render(request, "main/agency-detail.html", context)
