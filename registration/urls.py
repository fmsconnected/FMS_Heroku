from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
	path('New', views.registration_new, name='registration_new'),
	path('Registration/submit', views.registrationCreate, name='vRegistration_submit'),
	path('Details/<int:pk>', views.registrationDetails.as_view(), name='vregistration_details'),
	# path('VehicleMasterlist/Update/<int:pk>', vehicleMasterUpdate.as_view(),name='vehicle-update'),
	# path('VehicleMasterlist/Delete/<int:pk>', vehicleMasterlistDeleteView.as_view(), name='vehicleMasterlist_delete'),
	path('January', views.janRegView, name='registration_jan_reg'),
	path('Febuary', views.febRegView, name='registration_feb_reg'),
	path('March', views.marRegView, name='registration_mar_reg'),
	path('April', views.aprRegView, name='registration_apr_reg'),
	path('May', views.mayRegView, name='registration_may_reg'),
	path('June', views.junRegView, name='registration_jun_reg'),
	path('July', views.julRegView, name='registration_jul_reg'),
	path('August', views.augRegView, name='registration_aug_reg'),
	path('September', views.sepRegView, name='registration_sep_reg'),
	path('October', views.octRegView, name='registration_oct_reg'),
	path('Others', views.othersRegView, name='registration_others'),
	path('Trailer', views.trailerRegView, name='registration_trailer'),
	path('Update/<int:pk>', views.regUpdate, name='reg_update'),
	path('Summary/print/<int:pk>', views.registrationsPDFView.as_view(), name='registration_summary_print'),
	path('Summary/', views.summary, name = 'summary'),
	path('Email', views.HomeView, name="home_view"),
	# path('Reg/Month',views.emailfile, name="reg"),
	path('Reg/Excel', views.registration_excel, name="reg_excel"),
	]


