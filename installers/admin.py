from django.contrib import admin
from installers.models import User, Schedule

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
