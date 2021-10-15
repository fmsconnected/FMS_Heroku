from django.urls import path
from . import views
from .views import (
  	CarRentalDetailView,
	carrentalDeleteView,
	CarListView,
  	VehicleListView,
  	VehicleDetailView,
  	VehicleUpdateView,
	VehicleDeleteView,
  	FuelCreateView,
  	FuelUpdateView,
  	FuelListView,
	FuelDetailView,
	FuelDeleteView,
	
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
	path('Car/', CarListView.as_view(), name='carrental_list'),
	path('Car/Deadline', views.car_deadline, name='cardeadline'),
	path('Car/New', views.Carrentalpayment, name='Car-rental'),
	path('Car/Submit', views.Carrental_submit, name='Car_submit'),
	path('Car/Detail/<int:pk>', CarRentalDetailView.as_view(), name='Carrental_summary'),
	path('Car/Update/<int:pk>', views.Carrental_update, name='Car_update'),
	path('Car/Delete/<int:pk>', carrentalDeleteView.as_view(), name='carrental_delete'),
	path('Car/History/', views.carrentalHistoryView, name='carrental_history'),
	path('Car/export', views.car_excel, name = 'car_export'),
	path('Fuel/', FuelListView.as_view(), name = 'Fuel_supplierList'),
	path('Fuel/Deadline', views.fuel_deadline, name='fueldeadline'),
	path('Fuel/New', FuelCreateView.as_view(), name='Fuel_supplierNew'),
	path('Fuel/Update/<int:pk>', FuelUpdateView.as_view(), name='Fuel_update'),
	path('Fuel/Detail/<int:pk>', FuelDetailView.as_view(), name='Fuel-summary'),
	path('Fuel/Delete/<int:pk>', FuelDeleteView.as_view(), name='Fuel_delete'),
	path('Fuel/History/', views.FuelHistoryView, name='Fuel_history'),
	path('Fuel/export', views.fuel_excel, name='fuel_export'),
	path('VehicleRepair/', views.vrepair_payment.as_view(), name='vehiclerepair_payment'),
	path('VehicleRepair/New', views.vrepair_payment_create, name='vehiclerepair_payment_new'),
	path('VehicleRepair/Submit', views.vrepairsubmit, name='vehiclerepair_payment_submit'),
	path('VehicleRepair/Details/<int:pk>', views.vrepairDetailView.as_view(), name='vehicle_repair_details'),
	path('VehicleRepair/Update/<int:pk>', views.vrepairUpdate.as_view(), name='vehiclerepair_payment_udpate'),
	path('VehicleRepair/Delete/<int:pk>', views.vrepairDeleteView.as_view(), name='vehiclerepair_payment_delete'),
	path('VehicleRepair/export', views.vrepair_excel, name='vehiclerepair_payment_export'),
	path('VehicleRepair/History', views.vrepairlHistoryView, name='vehicle_repair_history'),
	path('Daily/Summary/', views.car_report_details, name='car_dailyreport_details'),
	path('Daily/Export/',views.car_report, name='car_dailyreport_export'),

]


