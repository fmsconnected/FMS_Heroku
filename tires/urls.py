from django.urls import path
from . import views
urlpatterns = [
    path('List/', views.tireListView.as_view(), name='tire_List'),
    path('Create/', views.tirecreate, name='tire_create'),
    path('Submit/', views.tiresubmit, name='tire_submit'),
    path('Delete/<int:pk>',views.tireDelete.as_view(), name='tire_delete'),
    path('Export/', views.tire_excel, name="tire_excel"),
    path('Update/<int:pk>', views.tireUpdateView.as_view(), name="tire_update"),
    path('Details/<int:pk>', views.tireDetailView.as_view(), name='tire_details'),
    path('Report/', views.tire_report, name='tirereport'),
    path('History/', views.tireHistoryView, name='tire_hitory'),
    path('Tire/', views.tire_deadline, name='tire_deadline'),
]
