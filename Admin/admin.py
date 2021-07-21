from django.contrib import admin
from .models import UserReport


@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ['id','action', 'username','date', 'ip', ]
    list_filter = ['id','date', ]
