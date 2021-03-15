
from django.urls import path
from . import views
from .views import (
	# employeeListView,
	employeeCreateView,
	employeeDetailView,
	employeeUpdateView,
	employeeMasterlistDeleteView,
	# vehicleMasterListView,
	# VmasterlistCreateView,
	vehicleMasterDetails,
	vehicleMasterUpdate,
	vehicleMasterlistDeleteView,
	leasing_export,
	)


urlpatterns = [
	# path('EmployeeMasterlist/', employeeListView.as_view(), name='employee-list'),
	path('EmployeeMasterlist/', views.empmastertables, name='employee-list'),
	path('EmployeeMasterlist/New', employeeCreateView.as_view(), name='employeeMasterlist-new'),
	path('EmployeeMasterlist/Detail/<int:pk>', employeeDetailView.as_view(), name='employee-details'),
	path('EmployeeMasterlist/Update/<int:pk>', employeeUpdateView.as_view(), name='employeeMasterlist-update'),
	path('EmployeeMasterlist/Delete/<int:pk>', employeeMasterlistDeleteView.as_view(), name='employeeMasterlist_delete'),
	path('EmployeeMasterlist/History/', views.employeeMasterlistHistoryView, name='employeeMasterlist_history'),
	path('Masterlist/export', views.employee_excel, name='masterlist_dl'),

	path('VehicleMasterlist/Active', views.vehicle_masterlist_active, name='vehicle_masterlist_active'),
	path('VehicleMasterlist/Solved', views.vehicle_masterlist_solved, name='vehicle_masterlist_solved'),
	path('VehicleMasterlist/Trans', views.vehicle_masterlist_trans, name='vehicle_masterlist_trans'),
	path('VehicleMasterlist/', views.Vmastertables, name='vehicle-list'),
	path('VehicleMasterlist/New', views.vehicle, name='vehicle_new'),
	path('VehicleMasterlist/submit', views.VmasterlistCreate, name='vehicleMasterlist_submit'),
	path('VehicleMasterlist/Details/<int:pk>', vehicleMasterDetails.as_view(), name='vehicle_details'),
	path('VehicleMasterlist/Update/<int:pk>', vehicleMasterUpdate.as_view(),name='vehicle-update'),
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
	#####Vehicle Leasing#####
	path('Leasing/', views.leasing, name='leasing_list'),
	path('Leasing/New', views.leasingCreateView.as_view(), name='leasing_new'),
	path('Leasing/Update/<int:pk>', views.leasingUpdateView.as_view(), name='leasing_update'),
	path('Leasing/Details/<int:pk>', views.leasingDetailView.as_view(), name='leasing_details'),
	path('Leasing/History', views.leasingHistoryView, name='leasing_history'),
	path('Leasing/Export', views.leasing_export, name='leasing_export'),
	path('Leasing/Active', views.vehicle_leasing_active, name='vehicle_leasing_active'),
	path('Leasing/Solved', views.vehicle_leasing_solved, name='vehicle_leasing_solved'),
	path('Leasing/Trans', views.vehicle_leasing_trans, name='vehicle_leasing_trans'),
	path('Vehicle/Teli/Export', views.vehicle_excel_teli, name='vehicleteli_export'),
	path('Leasing/Export/Active', views.leasing_active_export, name='leasing_active_export'),
	path('Leasing/Export/Sold', views.leasing_solved_export, name='leasing_solved_export'),
	path('Leasing/Export/Trans', views.leasing_trans_export, name='leasing_trans_export'),

]







