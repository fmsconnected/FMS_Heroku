from django.urls import path
from . import views

urlpatterns = [
	path('Request/', views.requestListView.as_view(), name='carrequest_list'),
	path('Request/New', views.requestCreate, name='car_request'),
	path('Request/Submit', views.requestsubmit, name='carrequest_submit'),
	path('Request/Details/<int:pk>/', views.requestDetailView.as_view(), name='carrequest_details'),
	path('Request/Update/<int:pk>/', views.requestUpdateView.as_view(), name='carrequest_update'),
	path('Request/Delete/<int:pk>/', views.requestDeleteView.as_view(), name='carrequest_delete'),
	path('Request/History/', views.requestHistoryView, name='carrequest_history'),
	path('Request/Export', views.car_request_excel, name='carrequest_export'),
	path('Gas/', views.gasListView.as_view(),name='gascard_list'),
	path('Gas/New', views.gascreate, name='gascard_new'),
	path('Gas/Submit', views.gassubmit, name='gas_submit'),
	path('Gas/Update/<int:pk>', views.gasUpdateView.as_view(), name='gascard_update'),
	path('Gas/Details/<int:pk>', views.gasDetailView.as_view(), name='gascard_details'),
	path('Gas/Delete/<int:pk>', views.gasDeleteView.as_view(), name='gascard_delete'),
	path('Gas/History/', views.gasHistoryView, name='gascard_history'),
	path('Gas/Export', views.gas_request_excel, name='gas_export'),
	path('Service/', views.serviceListView.as_view(), name='service_list'),
	path('Service/New', views.serviceCreate, name='service_new'),
	path('Service/Submit', views.servicesubmit, name='service_submit'),
	path('Service/Details/<int:pk>', views.serviceDetailView.as_view(), name='service_details'),
	path('Service/Update/<int:pk>', views.serviceUpdateView.as_view(), name='service_update'),
	path('Service/Delete/<int:pk>', views.serviceDeleteView.as_view(), name='service_delete'),
	path('Service/History/', views.serviceHistoryView, name='service_history'),
	path('Service/Export', views.service_request_excel, name='service_export'),
	path('Repair/', views.repairListView.as_view(), name='repair_list'),
	path('Repair/New', views.repairCreate, name="repair_new"),
	path('Repair/Submit', views.repairsubmit, name="repair_submit"),
	path('Repair/Details/<int:pk>', views.repairDetailView.as_view(), name='repair_details'),
	path('Repair/Update/<int:pk>', views.repairUpdateView.as_view(), name='repair_update'),
	path('Repair/Delete/<int:pk>', views.repairDeleteView.as_view(), name='repair_delete'),
	path('Repair/History/', views.repairHistoryView, name='repair_history'),
	path('Repair.Export', views.repair_request_excel, name='repair_export')

	]