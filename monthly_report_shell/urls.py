from django.urls import path
from . import views


urlpatterns = [
	path('MonthlyReport/Shell/List', views.monthly_report_shell, name = 'report_shell_list'),
	path('MonthlyReport/Shell/Details/<int:pk>', views.monthly_report_shellDetails.as_view(), name='report_shell_details'),
	
]


