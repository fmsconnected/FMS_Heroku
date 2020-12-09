
from django.urls import path
from . import views
from .views import (
    CSDetails,
    CSCreateView,
    CSUpdate,
    CSListView,
    CSDeleteView,
    customer_log_excel
)

urlpatterns = [
    path('', CSListView.as_view(), name='CS_List'),
    path('New', views.CSCreateView.as_view(), name='CS_new'),
    path('Update/<int:pk>',
         views.CSUpdate.as_view(), name='CS_update'),
    path('Details/<int:pk>',
         views.CSDetails.as_view(), name='CS_details'),
    path('Delete/<int:pk>',
         CSDeleteView.as_view(), name='CS_delete'),
    path('import', views.customer_log_excel, name="cs_import")
]
