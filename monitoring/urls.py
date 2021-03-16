from django.urls import path
from . import views

urlpatterns = [
	path('Monitoring/', views.monitoringListView.as_view(), name= 'Monitoring_list'),
	path('Monitoring/New', views.monitoring_create, name='Monitoring_new'),
	path('Monitoring/Submit', views.monitoring_submit, name='Monitoring_submit'),
	path('Monitoring/Update/<int:pk>', views.monitoringUpdate.as_view(), name='Monitoring_update'),
	path('Monitoring/Details/<int:pk>', views.monitoringDetails.as_view(), name='Monitoring_details'),
	path('Monitoring/Delete/<int:pk>', views.monitoringDeleteView.as_view(), name='Monitoring_delete'),
	path('Monitoring/History/', views.monitoringHistoryView, name='Monitoring_history'),
	# FILTER BY MONTH
	# path('Registration/January', views.janRegView, name='Monitoring_jan_reg'),
	# path('Registration/Febuary', views.febRegView, name='Monitoring_feb_reg'),
	# path('Registration/March', views.marRegView, name='Monitoring_mar_reg'),
	# path('Registration/April', views.aprRegView, name='Monitoring_apr_reg'),
	# path('Registration/May', views.mayRegView, name='Monitoring_may_reg'),
	# path('Registration/June', views.junRegView, name='Monitoring_jun_reg'),
	# path('Registration/July', views.julRegView, name='Monitoring_jul_reg'),
	# path('Registration/August', views.augRegView, name='Monitoring_aug_reg'),
	# path('Registration/September', views.sepRegView, name='Monitoring_sep_reg'),
	# path('Registration/October', views.octRegView, name='Monitoring_oct_reg'),
	# FILTER SUMMARY BY MONTH
	path('Summary/January', views.janSumView, name='Summary_jan_reg'),
	path('Summary/February', views.febSumView, name='Summary_feb_reg'),
	path('Summary/March', views.marSumView, name='Summary_mar_reg'),
	path('Summary/April', views.aprSumView, name='Summary_apr_reg'),
	path('Summary/May', views.maySumView, name='Summary_may_reg'),
	path('Summary/June', views.junSumView, name='Summary_jun_reg'),
	path('Summary/July', views.julSumView, name='Summary_jul_reg'),
	path('Summary/August', views.augSumView, name='Summary_aug_reg'),
	path('Summary/September', views.sepSumView, name='Summary_sep_reg'),
	path('Summary/October', views.octSumView, name='Summary_oct_reg'),
	# Summary Export
	path('Summary/Export/January', views.sum_jan_excel, name='sum_jan_export'),
	path('Summary/Export/Febuary', views.sum_feb_excel, name='sum_feb_export'),
	path('Summary/Export/March', views.sum_mar_excel, name='sum_mar_export'),
	path('Summary/Export/April', views.sum_apr_excel, name='sum_apr_export'),
	path('Summary/Export/May', views.sum_may_excel, name='sum_may_export'),
	path('Summary/Export/June', views.sum_jun_excel, name='sum_jun_export'),
	path('Summary/Export/July', views.sum_jul_excel, name='sum_jul_export'),
	path('Summary/Export/August', views.sum_aug_excel, name='sum_aug_export'),
	path('Summary/Export/September', views.sum_sep_excel, name='sum_sep_export'),
	path('Summary/Export/October', views.sum_oct_excel, name='sum_oct_export'),
	# FILTER WITHOUT TEMPLATE
	path('Plate-monitoring/', views.plateMonitoringView, name='Monitoring_plate'),
	path('Monitoring/Export', views.fata_excel, name='fata_export'),
	# path('Registration/Update/<int:pk>', views.regUpdate.as_view(), name='reg_update'),
	# FILTER BY Month Due
	path('Registration_Due/January', views.janReg_dueView, name='Monitoring_jan_reg_due'),
	path('Registration_Due/Febuary', views.febReg_dueView, name='Monitoring_feb_reg_due'),
	path('Registration_Due/March', views.marReg_dueView, name='Monitoring_mar_reg_due'),
	path('Registration_Due/April', views.aprReg_dueView, name='Monitoring_apr_reg_due'),
	path('Registration_Due/May', views.mayReg_dueView, name='Monitoring_may_reg_due'),
	path('Registration_Due/June', views.junReg_dueView, name='Monitoring_jun_reg_due'),
	path('Registration_Due/July', views.julReg_dueView, name='Monitoring_jul_reg_due'),
	path('Registration_Due/August', views.augReg_dueView, name='Monitoring_aug_reg_due'),
	path('Registration_Due/September', views.sepReg_dueView, name='Monitoring_sep_reg_due'),
	path('Registration_Due/October', views.octReg_dueView, name='Monitoring_oct_reg_due'),

	path('Registration_update/Update/<int:pk>', views.regUpdate, name='reg_due_update'),

]