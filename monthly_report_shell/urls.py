from django.urls import path
from . import views


urlpatterns = [
	path('MonthlyReport/Shell/List', views.monthly_report_shell, name = 'report_shell_list'),
	path('MonthlyReport/Shell/Summary/', views.reportsummary, name='report_summary'),
	path('MonthlyReport/Shell/Create/', views.shell_create.as_view(), name='shell_report_create'),
	path('MonthlyReport/Shell/Update/<int:pk>',views.shell_update.as_view(), name='shell_report_update'),
	path('MonthlyReport/Shell/Delete/<int:pk>',views.shell_delete.as_view(), name='shell_report_delete'),
	path('MonthlyReport/Shell/Detail/<int:pk>',views.shell_details.as_view(), name='shell_report_detail'),

]


