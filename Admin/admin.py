from django.contrib import admin
from .models import UserReport


@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip', ]
    list_filter = ['action', ]