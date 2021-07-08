from django.urls import path
from . import views


urlpatterns = [
	path('MonthlyReport/January', views.monthly_report_jan, name = 'jan_monthly_report'),
	path('MonthlyReport/January/Summary', views.monthly_report_jan_summary, name='report_jan_summary'),
	
]


