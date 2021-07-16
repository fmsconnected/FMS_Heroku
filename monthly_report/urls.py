from django.urls import path
from . import views


urlpatterns = [
	path('List', views.monthly_report_jan, name = 'jan_monthly_report'),
	path('Summary', views.monthly_report_jan_summary, name='report_jan_summary'),
	path('Create', views.petron_create.as_view(), name='petron_new'),
	path('Update/<int:pk>', views.petron_update.as_view(), name='petron_update'),
	path('Detail/<int:pk>', views.petron_details.as_view(), name='petron_detail'),
	path('Delete/<int:pk>', views.petron_delete.as_view(), name='petron_delete'),
]


