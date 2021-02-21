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
	path('Fcm/Update/<int:pk>', views.fleet_card_update.as_view(), name='Fcm_update'),
	path('Fcm/Delete/<int:pk>', views.fleet_card_delete.as_view(), name='Fcm_delete'),
	path('Fcm/export', views.fcm_export, name='fcm_export')

]