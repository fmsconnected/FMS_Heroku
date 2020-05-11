from django.urls import path
from . import views

urlpatterns = [
    path('Ownership/', views.ownershipListView.as_view(), name= 'ownership_list'),
    path('Ownership/Deadline', views.too_deadline, name='toodeadline'),
    path('Ownership/New', views.ownershipcreate, name='ownership_new'),
    path('Ownership/Submit', views.ownership_submit, name='ownership_submit'),
    path('Ownership/Update/<int:pk>', views.ownershipUpdate.as_view(), name='ownership_update'),
    path('Ownership/Details/<int:pk>', views.ownershipDetails.as_view(), name='ownership_details'),
    path('Ownership/Delete/<int:pk>', views.ownershipDeleteView.as_view(), name='ownership_delete'),
    path('Ownership/History/', views.ownershipHistoryView, name='ownership_history'),
    path('Ownership/Export', views.ownership_excel, name='ownership_export'),

    path('Billing/new', views.billing.as_view(), name='billing_new'),
    path('Billing/List', views.billing_list.as_view(), name='billing_list'),
    path('Billing/Details/<int:pk>', views.billingDetails.as_view(), name='billing_details'),
    path('Billing/Delete/<int:pk>', views.billingDeleteView.as_view(), name='billing_delete'),
    path('Billing/History', views.billingHistoryView, name='billing_history'),
    path('Billing/Update/<int:pk>', views.billingUpdate.as_view(), name='billing_update'),
    path('Billing/Export', views.billing_excel, name='billing_expo')

    ]