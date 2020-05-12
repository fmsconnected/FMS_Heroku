
from django.urls import path
from . import views

urlpatterns = [
	path('Leasing/', views.leasing, name='leasing_list'),
	path('Leasing/New', views.leasingCreateView.as_view(), name='leasing_new'),
	path('Leasing/Update/<int:pk>', views.leasingUpdateView.as_view(), name='leasing_update'),
	path('Leasing/Details/<int:pk>', views.leasingDetailView.as_view(), name='leasing_details'),
	path('Leasing/History', views.leasingHistoryView, name='leasing_history')
]







