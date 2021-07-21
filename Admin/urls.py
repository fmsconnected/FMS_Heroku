
from django.urls import path
from . import views
from .views import (
    user_report_excel,
    userListView,
)

urlpatterns = [
    path('User/export', views.user_report_excel, name='adminreport'),
    path('User/', userListView, name='user_list'),

]
