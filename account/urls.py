from django.urls import path
from . import views
from .views import (
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
    path('api/Petron/Report/', monthly_report_jan_summary.as_view()),
    path('api/monitoring/Reg/', views.reg.as_view()),
    path('api/monitoring/unReg/', views.unreg.as_view()),
    path('api/Masterlist/', views.masterlist.as_view()),
    path('api/Fleet/', views.fleet_card_all.as_view()),
    path('api/Plate/', views.plate_moniroting.as_view()),
    path('api/TMG/', views.lto_tmg.as_view()),
]
