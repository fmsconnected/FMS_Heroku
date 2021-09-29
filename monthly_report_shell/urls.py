from django.urls import path
from . import views


urlpatterns = [
	path('List', views.monthly_report_shell, name = 'report_shell_list'),
	path('Summary/', views.reportsummary, name='report_summary'),
	# path('Create/', views.shell_new.as_view(), name='shell_report_create'),
	# path('Update/<int:pk>',views.shell_update.as_view(), name='shell_report_update'),
	path('Delete/<int:pk>',views.shell_delete.as_view(), name='shell_report_delete'),
	path('Detail/<int:pk>',views.shell_details.as_view(), name='shell_report_detail'),
	path('Shell/Export', views.shellreport_export, name='shell_export'),

]


