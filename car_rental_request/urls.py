from django.urls import path
from . import views

urlpatterns = [
	path('Request/', views.requestListView.as_view(), name='carrequest_list'),
	path('Request/Deadline', views.crr_deadline, name='crrdeadline'),
	path('Request/New', views.requestCreate, name='car_request'),
	path('Request/Submit', views.requestsubmit, name='carrequest_submit'),
	path('Request/Details/<int:pk>/', views.requestDetailView.as_view(), name='carrequest_details'),
	path('Request/Update/<int:pk>/', views.requestUpdateView.as_view(), name='carrequest_update'),
	path('Request/Delete/<int:pk>/', views.requestDeleteView.as_view(), name='carrequest_delete'),
	path('Request/History/', views.requestHistoryView, name='carrequest_history'),
	path('Request/Export', views.car_request_excel, name='carrequest_export'),
	]