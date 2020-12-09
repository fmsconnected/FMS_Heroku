
from django.urls import path
from . import views
from .views import (
    CSDetails,
    CSCreateView,
    CSUpdate,
    CSListView,
    CSDeleteView
)

urlpatterns = [
    path('', CSListView.as_view(), name='CS_List'),
    path('CS/New', views.CSCreateView.as_view(), name='CS_new'),
    path('CS/Update/<int:pk>',
         views.CSUpdate.as_view(), name='CS_update'),
    path('CS/Details/<int:pk>',
         views.CSDetails.as_view(), name='CS_details'),
    path('CS/Delete/<int:pk>',
         CSDeleteView.as_view(), name='CS_delete'),
]
