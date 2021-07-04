from django.urls import path
from . import views

urlpatterns = [
	path('Corrective/', views.correctiveListView.as_view(), name='corrective_list'),
	path('Corrective/New', views.correctiveCreate, name='corrective_create'),
	path('Corrective/Submit', views.correctivesubmit, name='corrective_submit'),
	path('Corrective/Details/<int:pk>/', views.correctiveDetailView.as_view(), name='corrective_details'),
	path('Corrective/Update/<int:pk>/', views.correctiveUpdateView.as_view(), name='corrective_update'),
	path('Corrective/Delete/<int:pk>/', views.correctiveDeleteView.as_view(), name='corrective_delete'),
	path('Corrective/History', views.correctiveHistoryView, name='corrective_history'),
	path('Corrective/Export', views.corrective_excel, name='corrective_export'),
	path('Corrective/Report/Details',views.vehicle_maintenance_report_details, name='v_maitenance_details'),
	path('Corrective/Report/Export', views.vehicle_maintenance_report, name='v_maitenance_report'),

	]