
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from ajax_select import urls as ajax_select_urls
from django.conf.urls import url, include
from rest_framework import routers
from masterlist import views


admin.autodiscover()
router = routers.DefaultRouter()
# router.register(r'masterlist', views.vehicleViewSet),
router.register(r'empmasterlist', views.employeeViewSet),

from leasingmasterlist import views
router.register(r'Leasing_Masterlist', views.leasingViewSet),

from vehicle_masterlist import views
router.register(r'Vehicle_Masterlist', views.vehicleViewSet),


from monitoring import views
router.register(r'monitoring', views.monitoringViewSet),

from monthly_report import views
router.register(r'MonthlyReport', views.petronViewSet),

from monthly_report_shell import views
router.register(r'MonthlyReportShell', views.shell_report_ViewSet),

urlpatterns = [
    url('^api/', include(router.urls)),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^admin/', admin.site.urls),
    path('FLEET/', include('account.urls')),
    path('Payment/', include('payment.urls')),
    path('Masterlist/', include('masterlist.urls')),
    path('Leasing/', include('leasingmasterlist.urls')),
    path('VehicleMasterlist/', include('vehicle_masterlist.urls')),
    path('Monitoring/', include('monitoring.urls')),
    path('Request/', include('request.urls')),
    path('Ownership/', include('ownership.urls')),
    path('Report/', include('report.urls')),
    path('Admin/', include('Admin.urls')),
    path('Corrective/', include('corrective.urls')),
    path('Customer/', include('CustomerLog.urls')),
    path('Fcm/', include('fleet_card.urls')),
    path('Registration/', include('registration.urls')),
    path('Monthly/Report/', include('monthly_report.urls')),
    path('Monthly/Report/Shell/', include('monthly_report_shell.urls')),
    path('', auth_views.LoginView.as_view(
        template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
