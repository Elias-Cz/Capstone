import datetime
import random

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from calendar import monthrange

from .models import User, Schedule, Day

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
                return HttpResponseRedirect(reverse("profile"))
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
    user = request.user
    if user.installer == True:
        a = get_object_or_404(Day, installer=user)
        c = a.customer
        d = a.day_data
        return render(request, "installers/profile.html", {
        "c": c,
        "d": d
        })
    elif user.installer == False:
        appointment_check = Day.objects.filter(customer=user)
        # Check for past appointments, list past projects
        if not appointment_check:
            projects = "No projects scheduled"
            appointment_check = False
        else:
            a = get_object_or_404(Day, customer=user)
            projects = a.day_data
            appointment_check = True
        return render(request, "installers/profile.html", {
        "projects": projects,
        "appointment_check": appointment_check
        })

def schedule(request):
    dt = datetime.datetime.today()
    month_ref = dt.month
    year_ref = dt.year
    day_range = monthrange(year_ref, month_ref)
    day_range_add = day_range[1] + 1
    range_len = list(range(1, day_range_add))
    begining_day = day_range[0]
    date_offset = list(range(0, day_range[0]))
    print(date_offset)
    print(days[begining_day])
    print(range_len)
    if request.method == "POST":
        date = request.POST.get('date_value')
        month_num = request.POST.get('month_name')
        user = get_object_or_404(User, username=request.user)
        date_month = month_num + '' + date
        print(date_month)
        installer_check = User.objects.filter(installer=True)
        installer = random.choice(installer_check)
        print(installer_check)
        d = Day(day_data=date_month, customer=user, installer=installer)
        d.save()
        date_new = get_object_or_404(Day, day_data=date_month)
        s = Schedule(date_data=date_new, user_appointment=user)
        s.save()
        print('saved appt')
        return render(request, "installers/confirm.html", {
        "month": month_num,
        "date": date,
        })
    return render(request, "installers/schedule.html", {
    "range_len": range_len,
    "date_offset": date_offset
    })

def confirm(request):
    pass

def appointments(request):
    day = get_object_or_404(Day, customer=request.user)
    dates = day.day_data
    installer = day.installer


    return render(request, "installers/appointments.html", {
    "dates": dates,
    "installer": installer
    })



def installer(request):
    username = request.user
    check_perms = get_object_or_404(User, username=username)
    if check_perms.installer == False:
        return render(request, "installers/index.html", {
        "message_2": "The page you are requesting is restricted"
        })
    elif check_perms.installer == True:
        return render(request, "installers/profile.html")
