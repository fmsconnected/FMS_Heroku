from django.urls import path
from . import views

urlpatterns = [
    path('New', views.registration_new, name='registration_new'),
    path('Registration/submit', views.registrationCreate,
         name='vRegistration_submit'),
    path('Details/<int:pk>', views.registrationDetails.as_view(),
         name='vregistration_details'),
    # path('Update/<int:pk>', views.regUpdate, name='reg_update'),
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
    path('Update/<int:pk>', views.regUpdate.as_view(), name='reg_update'),
    path('Summary/print/<int:pk>', views.registrationsPDFView.as_view(),
         name='registration_summary_print'),
    path('Summary/', views.summary, name='summary'),
    path('Registration/Daily/Report', views.registration_report_detail,
         name="reg_dailyreport_detail"),
    path('Registration/Excel', views.registration_excel, name="reg_excel"),
    path('Registration/Report', views.registration_report, name="reg_report"),
]
