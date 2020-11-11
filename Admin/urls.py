
from django.urls import path
from . import views
from .views import (
    user_report_excel
)

urlpatterns = [
    path('Admin/export', views.user_report_excel, name='adminreport'),
]
