from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('schedule', views.schedule, name='schedule'),
    path('installer', views.installer, name="installer"),
    path('appointments', views.appointments, name='appointments'),
    path('confirm', views.confirm, name="confirm")
]
