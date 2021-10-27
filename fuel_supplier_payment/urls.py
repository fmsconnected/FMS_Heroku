from django.urls import path
from . import views
from .views import (
  	FuelCreateView,
  	FuelUpdateView,
  	FuelListView,
	FuelDetailView,
	FuelDeleteView,
	
 )

urlpatterns = [
	path('Fuel/', FuelListView.as_view(), name = 'Fuel_supplierList'),
	path('Fuel/Deadline', views.fuel_deadline, name='fueldeadline'),
	path('Fuel/New', FuelCreateView.as_view(), name='Fuel_supplierNew'),
	path('Fuel/Update/<int:pk>', FuelUpdateView.as_view(), name='Fuel_update'),
	path('Fuel/Detail/<int:pk>', FuelDetailView.as_view(), name='Fuel-summary'),
	path('Fuel/Delete/<int:pk>', FuelDeleteView.as_view(), name='Fuel_delete'),
	path('Fuel/History/', views.FuelHistoryView, name='Fuel_history'),
	path('Fuel/export', views.fuel_excel, name='fuel_export'),
	path('Fuel/Ongoing', views.Fuel_ongoing, name='fuel_ongoing'),
	path('Fuel/Completed', views.Fuel_completed, name='fuel_completed'),

]


