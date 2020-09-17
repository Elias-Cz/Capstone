import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from calendar import monthrange

from .models import User

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

def index(request):
    return render(request, "installers/index.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "installers/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "installers/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("profile"))
    else:
        return render(request, "installers/register.html")

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            check_perms = get_object_or_404(User, username=username)
            if check_perms.installer == True:
                print('yay')
                login(request, user)
                return HttpResponseRedirect(reverse("installer"))
            if check_perms.installer == False:
                print('no')
                login(request, user)
                return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "installers/index.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "installers/index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def profile(request):
    return render(request, "installers/profile.html")

def schedule(request):
    day_range = monthrange(2020, 9)
    day_range_add = day_range[1] + 1
    range_len = list(range(1, day_range_add))
    begining_day = day_range[0]
    date_offset = list(range(0, day_range[0]))
    print(date_offset)
    print(days[begining_day])
    print(range_len)
    return render(request, "installers/schedule.html", {
    "range_len": range_len,
    "date_offset": date_offset
    })

def activate(request):
    if request.method == "POST":
        employee_id = request.POST.get('emp_id')
        employee_id = int(employee_id)
        print(employee_id)
        print(type(employee_id))
        user = request.user
        employee_ids = list(range(1000, 1200))
        if employee_id in employee_ids:
            User.objects.filter(username=user).update(installer=True)
            return HttpResponseRedirect(reverse("installer"))
        else:
            return render(request, "installers/activate.html", {
            "message": "Invalid employee ID"
            })
    return render(request, "installers/activate.html")

def installer(request):
    username = request.user
    check_perms = get_object_or_404(User, username=username)
    if check_perms.installer == False:
        return render(request, "installers/index.html", {
        "message_2": "The page you are requesting is restricted"
        })
    elif check_perms.installer == True:
        return render(request, "installers/installer_profile.html")
