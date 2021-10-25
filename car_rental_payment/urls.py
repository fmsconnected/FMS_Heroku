from django.urls import path
from . import views
from .views import (
  	CarRentalDetailView,
	carrentalDeleteView,
	CarListView,
	
 )

urlpatterns = [
	path('Car/', CarListView.as_view(), name='carrental_list'),
	path('Car/Deadline', views.car_deadline, name='cardeadline'),
	path('Car/New', views.Carrentalpayment, name='Car-rental'),
	path('Car/Submit', views.Carrental_submit, name='Car_submit'),
	path('Car/Detail/<int:pk>', CarRentalDetailView.as_view(), name='Carrental_summary'),
	path('Car/Update/<int:pk>', views.Carrental_update, name='Car_update'),
	path('Car/Delete/<int:pk>', carrentalDeleteView.as_view(), name='carrental_delete'),
	path('Car/History/', views.carrentalHistoryView, name='carrental_history'),
	path('Car/export', views.car_excel, name = 'car_export'),
	path('Daily/Summary/', views.car_report_details, name='car_dailyreport_details'),
	path('Daily/Export/',views.car_report, name='car_dailyreport_export'),
	path('Car/Ongoing', views.car_ongoing, name='car_ongoing'),
	path('Car/Completed', views.car_completed, name='car_completed'),

]


