
from django.urls import path
from . import views


urlpatterns = [
	#####Vehicle Leasing#####
	path('Leasing/', views.leasing, name='leasing_list'),
	path('Leasing/New', views.leasingCreateView.as_view(), name='leasing_new'),
	path('Leasing/Update/<int:pk>', views.leasingUpdateView.as_view(), name='leasing_update'),
	path('Leasing/Details/<int:pk>', views.leasingDetailView.as_view(), name='leasing_details'),
	path('Leasing/History', views.leasingHistoryView, name='leasing_history'),
	path('Leasing/Export', views.leasing_export, name='leasing_export'),
	path('Leasing/Active', views.vehicle_leasing_active, name='vehicle_leasing_active'),
	path('Leasing/Solved', views.vehicle_leasing_solved, name='vehicle_leasing_solved'),
	path('Leasing/Trans', views.vehicle_leasing_trans, name='vehicle_leasing_trans'),
	path('Leasing/Export/Active', views.leasing_active_export, name='leasing_active_export'),
	path('Leasing/Export/Sold', views.leasing_solved_export, name='leasing_solved_export'),
	path('Leasing/Export/Trans', views.leasing_trans_export, name='leasing_trans_export'),

]







