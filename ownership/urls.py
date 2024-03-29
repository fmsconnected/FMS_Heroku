from django.urls import path
from . import views

urlpatterns = [
    path('Ownership/', views.ownershipListView.as_view(), name= 'ownership_list'),
    path('Ownership/Deadline', views.too_deadline, name='toodeadline'),
    path('Ownership/New', views.ownershipcreate, name='ownership_new'),
    path('Ownership/New/Bidder', views.bidder.as_view(), name='ownership_bidder'),
    path('Ownership/Submit', views.ownership_submit, name='ownership_submit'),
    path('Ownership/Update/<int:pk>', views.ownershipUpdate.as_view(), name='ownership_update'),
    path('Ownership/Details/<int:pk>', views.ownershipDetails.as_view(), name='ownership_details'),
    path('Ownership/Delete/<int:pk>', views.ownershipDeleteView.as_view(), name='ownership_delete'),
    path('Ownership/History/', views.ownershipHistoryView, name='ownership_history'),
    path('Ownership/Export', views.ownership_excel, name='ownership_export'),
    path('Ownership/Report', views.ownership_report, name='ownership_report'),
    path('Ownership/Report/Details', views.ownership_report_details, name='ownership_report_details'),
    path('Ownership/Ongoing', views.ownership_ongoing, name="ownership_ongoing"),
    path('Ownership/Completed', views.ownership_completed, name="ownership_completed"),
    path('Ownership/Date_application', views.date_application, name="date_application"),

    path('Billing/new', views.billing.as_view(), name='billing_new'),
    path('Billing/List', views.billing_list.as_view(), name='billing_list'),
    path('Billing/Details/<int:pk>', views.billingDetails.as_view(), name='billing_details'),
    path('Billing/Delete/<int:pk>', views.billingDeleteView.as_view(), name='billing_delete'),
    path('Billing/History', views.billingHistoryView, name='billing_history'),
    path('Billing/Update/<int:pk>', views.billingUpdate.as_view(), name='billing_update'),
    path('Billing/Export', views.billing_excel, name='billing_expo'),

    ]