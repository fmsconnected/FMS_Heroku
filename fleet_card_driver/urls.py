from django.urls import path
from . import views


urlpatterns = [
	
	path('FCD_list', views.fleetcarddriver_list.as_view(), name='FCD_list'),
	path('FCD_new', views.fleetcarddriver_create.as_view(), name='FCD_new'),
	path('Update/<int:pk>', views.fleetcarddriver_update.as_view(), name='FCD_update'),
	path('Delete/<int:pk>', views.fleetcarddriver_delete.as_view(), name='FCD_delete'),
	path('export', views.fcd_export, name='FCD_export'),
	path('FCD/Ongoing', views.fleetcarddriver_ongoing.as_view(), name="FCD_ongoing"),
	path('FCD/Completed', views.fleetcarddriver_completed.as_view(), name="FCD_completed"),
	# path('Daily/Report/Export', views.fleet_report, name='daily_report'),
	# path('Daily/Summary/', views.fleet_summary, name='daily_summary'),

]