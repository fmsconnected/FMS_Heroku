from django.urls import path
from . import views

urlpatterns = [
	path('Gas/', views.gasListView.as_view(),name='gascard_list'),
	path('Gas/Deadline', views.gcc_deadline, name='gccdeadline'),
	path('Gas/New', views.gascreate, name='gascard_new'),
	path('Gas/Submit', views.gassubmit, name='gas_submit'),
	path('Gas/Update/<int:pk>', views.gasUpdateView.as_view(), name='gascard_update'),
	path('Gas/Details/<int:pk>', views.gasDetailView.as_view(), name='gascard_details'),
	path('Gas/Delete/<int:pk>', views.gasDeleteView.as_view(), name='gascard_delete'),
	path('Gas/History/', views.gasHistoryView, name='gascard_history'),
	path('Gas/Export', views.gas_request_excel, name='gas_export'),
	path('Repair/', views.repairListView, name='repair_list'),
	path('Repair/Deadline', views.vrp_deadline, name='vrpdeadline'),
	path('Repair/New', views.repairCreate, name="repair_new"),
	path('Repair/Submit', views.repairsubmit, name="repair_submit"),
	path('Repair/Details/<int:pk>', views.repairDetailView.as_view(), name='repair_details'),
	path('Repair/Update/<int:pk>', views.repairUpdateView.as_view(), name='repair_update'),
	path('Repair/Delete/<int:pk>', views.repairDeleteView.as_view(), name='repair_delete'),
	path('Repair/History/', views.repairHistoryView, name='repair_history'),
	path('Repair.Export', views.repair_request_excel, name='repair_export'),
	path('Repair/Report/Details',views.vehicle_maintenance_report_details, name='maitenance_details'),
	path('Repair/Report/Export', views.vehicle_maintenance_report, name='maitenance_report'),
	]