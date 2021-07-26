from django.urls import path
from . import views
urlpatterns = [
    path('List/', views.batteryListView.as_view(), name='battery_List'),
    path('Create/', views.batterycreate, name='battery_create'),
    path('Submit/', views.batterysubmit, name='battery_submit'),
    path('Delete/<int:pk>',views.batteryDelete.as_view(), name='battery_delete'),
    path('Export/', views.battery_excel, name="battery_excel"),
    path('Update/<int:pk>', views.batteryUpdateView.as_view(), name="battery_update"),
    path('Details/<int:pk>', views.batteryDetailView.as_view(), name='battery_details'),
    path('Report/', views.battery_report, name='batteryreport'),
    path('History/', views.batteryHistoryView, name='battery_hitory'),
]
