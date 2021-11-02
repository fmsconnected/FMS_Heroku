from django.urls import path
from . import views

urlpatterns = [
	path('Report/', views.reportListView.as_view(), name= 'report_list'),
	path('Report/Deadline', views.report_deadline, name='reportdeadline'),
	path('Report/New', views.report_new, name='report_new'),
	path('Report/Submit', views.report_submit, name='report_submit'),
	path('Report/Export', views.report_excel, name='report_export'),
	path('Report/Update/<int:pk>', views.reportUpdate.as_view(), name='report_update'),
	path('Report/Details/<int:pk>', views.reportDetails.as_view(), name='insurancereport_details'),
	path('Report/Delete/<int:pk>', views.reportDeleteView.as_view(), name='report_delete'),
	path('Report/History/', views.reportHistoryView, name='report_history'),
	path('Report/Ongoing', views.report_ongoing, name= 'report_ongoing'),
	path('Report/Completed', views.report_completed, name= 'report_completed'),

]