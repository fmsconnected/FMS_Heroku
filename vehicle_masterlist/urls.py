
from django.urls import path
from . import views
from .views import (
	vehicleMasterDetails,
	vehicleMasterUpdate,
	vehicleMasterlistDeleteView,
	)


urlpatterns = [

	path('VehicleMasterlist/Active', views.vehicle_masterlist_active, name='vehicle_masterlist_active'),
	path('VehicleMasterlist/Solved', views.vehicle_masterlist_solved, name='vehicle_masterlist_solved'),
	path('VehicleMasterlist/Trans', views.vehicle_masterlist_trans, name='vehicle_masterlist_trans'),
	path('VehicleMasterlist/Globe', views.vehicle_masterlist_globe, name='vehicle_masterlist_globe'),
	path('VehicleMasterlist/', views.Vmastertables, name='vehicle-list'),
	path('VehicleMasterlist/New', views.vehicle, name='vehicle_new'),
	path('VehicleMasterlist/submit', views.VmasterlistCreate, name='vehicleMasterlist_submit'),
	path('VehicleMasterlist/Details/<int:pk>', vehicleMasterDetails.as_view(), name='vehicle_details'),
	path('VehicleMasterlist/Confirmation/<int:pk>',views.confirmationDetails.as_view(),name='con_details'),
	path('VehicleMasterlist/Update/<int:pk>', vehicleMasterUpdate.as_view(),name='vehicle-update'),
	path('VehicleMasterlist/Status/Update/<int:pk>', views.vmUpdate, name='vehicle_status'),
	path('VehicleMasterlist/Delete/<int:pk>', vehicleMasterlistDeleteView.as_view(), name='vehicleMasterlist_delete'),
	path('VehicleMasterlist/History/', views.vehicleMasterlistHistoryView, name='vehicleMasterlist_history'),
	path('Vehicle/<int:pk>', views.releaseUpdate.as_view(), name='vupdate'),
	path('Vehiclelist/export', views.vehicle_excel, name='vehiclelist_export'),
	path('Vehiclelist/export/Active', views.vehicle_excel_active, name='vehicle_excel_active'),
	path('Vehiclelist/export/Sold', views.vehicle_excel_solved, name='vehicle_excel_solved'),
	path('Vehiclelist/export/Transferred', views.vehicle_excel_trans, name='vehicle_excel_trans'),
	path('Registration/Details/<int:pk>', views.vreg_details.as_view(), name='vregistration_details'),
	######Vehicle Bayantel FIlter########
	path('Vehicle/Bayantel', views.vehicle_bayan, name='vehicle_bayantel'),
	path('Vehicle/Bayan/Export', views.vehicle_excel_bayan, name='vehiclebayan_export'),
	#####Vehicle vehicle_telicphil ###
	path('Vehicle/Telicphil', views.vehicle_telicphil, name='vehicle_teli'),
	path('Vehicle/Teli/Export', views.vehicle_excel_teli, name='vehicleteli_export'),


]



