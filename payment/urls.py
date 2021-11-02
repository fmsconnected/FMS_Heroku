from django.urls import path
from . import views


urlpatterns = [
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
	path('VehicleRepair/Ongoing', views.vrp_ongoing, name="vrp_ongoing"),
	path('VehicleRepair/Completed', views.vrp_completed, name="vrp_completed"),

]


