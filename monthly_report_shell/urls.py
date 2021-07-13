from django.urls import path
from . import views


urlpatterns = [
	path('MonthlyReport/Shell/List', views.monthly_report_shell, name = 'report_shell_list'),
	path('MonthlyReport/Shell/Summary/', views.monthly_report_shellDetails, name='report_shell_details'),
	path('MonthlyReport/Shell/Create/', views.shell_create.as_view(), name='shell_report_create'),

]


