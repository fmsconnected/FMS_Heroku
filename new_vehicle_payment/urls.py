from django.urls import path
from . import views
from .views import (
  	VehicleListView,
  	VehicleDetailView,
  	VehicleUpdateView,
	VehicleDeleteView,
	
 )

urlpatterns = [
	path('Vehicle/', VehicleListView.as_view(), name = 'Vehicle_list'),
	path('Vehicle/Deadline', views.nvp_deadline,name='Vehicle_deadline'),
	path('Vehicle/New', views.vehiclecreate, name='Vehicle-new'),
	path('Vehicle/submit', views.vehicle_submit, name='Vehicle_submit'),
	path('Vehicle/Detail/<int:pk>', VehicleDetailView.as_view(), name='Vehicle-summary'),
	path('Vehicle/Update/<int:pk>', VehicleUpdateView.as_view(), name='Vehicle-update'),
	path('Vehicle/Delete/<int:pk>', VehicleDeleteView.as_view(), name='Vehicle_delete'),
	path('Vehicle/History/', views.VehicleHistoryView, name='Vehicle_history'),
	path('Vehicle/export', views.vehicle_excel, name='vehicle_export'),
	path('Daily/Summary/', views.car_report_details, name='car_dailyreport_details'),
	path('Daily/Export/',views.car_report, name='car_dailyreport_export'),
	path('Vehicle/Ongoing',views.vehicle_completed, name='vehicle_completed'),
	path('Vehicle/Completed',views.vehicle_ongoing, name='vehicle_ongoing'),

]


