
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
	# path('VehicleMasterlist/', views.vehicleMasterListView.as_view(), name='vehicle-list'),
	# path('VehicleMasterlist/', views.vehicle_list, name='vehicle-list'),
	path('VehicleMasterlist/', views.Vmastertables, name='vehicle-list'),
	path('VehicleMasterlist/New', views.vehicle, name='vehicle_new'),
	path('VehicleMasterlist/submit', views.VmasterlistCreate, name='vehicleMasterlist_submit'),
	path('VehicleMasterlist/Details/<int:pk>', vehicleMasterDetails.as_view(), name='vehicle_details'),
	path('VehicleMasterlist/Update/<int:pk>', vehicleMasterUpdate.as_view(),name='vehicle-update'),
	path('VehicleMasterlist/Delete/<int:pk>', vehicleMasterlistDeleteView.as_view(), name='vehicleMasterlist_delete'),
	path('VehicleMasterlist/History/', views.vehicleMasterlistHistoryView, name='vehicleMasterlist_history'),
	path('Vehicle/<int:pk>', views.releaseUpdate.as_view(), name='vupdate'),
	path('Vehiclelist/export', views.vehicle_excel, name='vehiclelist_export'),
	path('Registration/Details/<int:pk>', views.vreg_details.as_view(), name='vregistration_details'),
	######Vehicle Bayantel FIlter########
	path('Vehicle/Bayantel', views.vehicle_bayan, name='vehicle_bayantel'),
	path('Vehicle/Bayan/Export', views.vehicle_excel_bayan, name='vehiclebayan_export'),
	#####Vehicle vehicle_telicphil ###
	path('Vehicle/Telicphil', views.vehicle_telicphil, name='vehicle_teli'),
	path('Vehicle/Teli/Export', views.vehicle_excel_teli, name='vehicleteli_export'),
	#####Vehicle Leasing#####
	# path('Vehicle/Leasing', views.vehicle_leasing, name='vehicle_leasing'),
	# path('Vehicle/Leasing/Export', views.vehicle_excel_leasing, name='leasing_export'),
	# path('Vehicle/filter', views.registration, name='vehiclefilter'),
	path('Leasing/', views.leasing, name='leasing_list'),
	path('Leasing/New', views.leasingCreateView.as_view(), name='leasing_new'),
	path('Leasing/Update/<int:pk>', views.leasingUpdateView.as_view(), name='leasing_update'),
	path('Leasing/Details/<int:pk>', views.leasingDetailView.as_view(), name='leasing_details')
]







