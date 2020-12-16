from django.urls import path
from django.conf.urls import url
from . import views
from .views import HomeView, ChartData,Vmasterlist,Emasterlist,Lmasterlist

urlpatterns = [
    # path('', views.index, name='FLEET-index')
    path('', HomeView.as_view(), name='FLEET-index'),
    path('api/monitoring/', ChartData.as_view()),
    path('api/Vmonitoring/', Vmasterlist.as_view()),
    path('api/Emonitoring/', Emasterlist.as_view()),
    path('api/Lmonitoring/', Lmasterlist.as_view())
]