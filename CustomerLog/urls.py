from django.urls import path
from . import views
from .views import (
    CSDetails,
    CSCreateView,
    CSUpdate,
    CSListView,
    CSDeleteView,
    customer_log_excel,
    CS_deadline,
    CSpending
)
urlpatterns = [
    path('', views.CSListView, name='CS_List'),
    path('New', views.CSCreateView.as_view(), name='CS_new'),
    path('Update/<int:pk>', views.CSUpdate, name='CS_update'),
    path('Details/<int:pk>', views.CSDetails.as_view(), name='CS_details'),
    path('Delete/<int:pk>', CSDeleteView.as_view(), name='CS_delete'),
    path('Import', views.customer_log_excel, name="cs_import"),
    path('Deadline', views.CS_deadline, name="cs_deadline"),
    path('Pending', views.CSpending, name="CS_pending")
]
