from django.urls import path
from . import views

urlpatterns = [
	path('Service/', views.serviceListView.as_view(), name='service_list'),
	path('Service/Deadline', views.svr_deadline, name='svrdeadline'),
	path('Service/New', views.serviceCreate, name='service_new'),
	path('Service/Submit', views.servicesubmit, name='service_submit'),
	path('Service/Details/<int:pk>', views.serviceDetailView.as_view(), name='service_details'),
	path('Service/Update/<int:pk>', views.serviceUpdateView.as_view(), name='service_update'),
	path('Service/Delete/<int:pk>', views.serviceDeleteView.as_view(), name='service_delete'),
	path('Service/History/', views.serviceHistoryView, name='service_history'),
	path('Service/Export', views.service_request_excel, name='service_export'),
	path('Service/Daily/Report', views.service_report, name='service_vehicle_report'),
	path('Service/Daily/Export', views.service_vehicle_report, name='service_daily_export'),
	
	]