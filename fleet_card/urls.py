from django.urls import path
from . import views
from .views import (
  	fleet_card_list,
	fleet_card_create,
	fleet_card_update,
  	fleet_card_delete
 )

urlpatterns = [
	
	path('Fcm_list', views.fleet_card_list.as_view(), name='Fcm_list'),
	path('Fcm_new', views.fleet_card_create.as_view(), name='Fcm_new'),
	path('Update/<int:pk>', views.fleet_card_update.as_view(), name='Fcm_update'),
	path('Delete/<int:pk>', views.fleet_card_delete.as_view(), name='Fcm_delete'),
	path('export', views.fcm_export, name='fcm_export'),
	path('Details/<int:pk>', views.fleet_cardDetails.as_view(), name="fcm_details"),
	path('Daily/Report/Export', views.fleet_report, name='daily_report'),
	path('Daily/Summary/', views.fleet_summary, name='daily_summary'),
	path('Ongoing/', views.fcm_ongoing, name="fcm_ongoing"),
	path('Completed/', views.fcm_completed, name="fcm_completed"),

]