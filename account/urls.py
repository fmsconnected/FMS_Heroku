from django.urls import path
from django.conf.urls import url
from . import views
from .views import  (
	ChartData,
	ChartData_ongoing,
	ChartData_completed,
	Vmasterlist,
	Emasterlist,
	Lmasterlist,
	monthly_report_jan_summary,
    # monthly_report_shell_summary
	)

urlpatterns = [
    path('', views.index, name='FLEET-index'),
    # path('', HomeView.as_view(), name='FLEET-index'),
    path('api/monitoring/', ChartData.as_view()),
    path('api/monitoring/Ongoing/', ChartData_ongoing.as_view()),
    path('api/monitoring/Completed/', ChartData_completed.as_view()),
    path('api/Vmonitoring/', Vmasterlist.as_view()),
    path('api/Emonitoring/', Emasterlist.as_view()),
    path('api/Lmonitoring/', Lmasterlist.as_view()),
    path('api/Petron/Report/',monthly_report_jan_summary.as_view()),
    # path('api/Shell/Report/', monthly_report_shell_summary.as_view()),
]