
import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'xm#bo4qsr2hahkrtiaga=@xa2xvi7ecrj1utnsramtbu-4g1&3'
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['fmsjxmtsi.herokuapp.com']
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_datatables',
    'ajax_select',
    'bootstrap_modal_forms',
    'widget_tweaks',
    'simple_history',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'django_celery_beat',
    'django_crontab',
    'schedule',
    'mailer',
    'crispy_forms',
    'mathfilters',
    'django.contrib.humanize',
    'account.apps.AccountConfig',
    'payment.apps.paymentConfig',
    'masterlist.apps.MasterlistConfig',
    'monitoring.apps.MonitoringConfig',
    'request.apps.RequestConfig',
    'ownership.apps.OwnershipConfig',
    'report.apps.ReportConfig',
    'leasingmasterlist.apps.LeasingmasterlistConfig',
    'corrective.apps.CorrectiveConfig',
    'Admin.apps.AdminConfig',
    'CustomerLog.apps.CustomerlogConfig',
    'fleet_card.apps.FleetCardConfig',
    'registration.apps.RegistrationConfig',
    'vehicle_masterlist.apps.VehicleMasterlistConfig',
    'monthly_report.apps.MonthlyReportConfig',
    'monthly_report_shell.apps.MonthlyReportShellConfig',
    'battery.apps.BatteryConfig',
    'tires.apps.TiresConfig',
    'car_rental_payment.apps.CarRentalPaymentConfig',
    'car_rental_request.apps.CarRentalRequestConfig',
    'service_request.apps.ServiceRequestConfig',
    'new_vehicle_payment.apps.NewVehiclePaymentConfig',
    

]
# AUTHENTICATION_BACKENDS = (
#     'django_python3_ldap.auth.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

# AUTH_USER_MODEL = "Admin.AllLogin"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    
]

# opional, as this will log you out when browser is closed
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# 0r 5 * 60, same thing
# SESSION_COOKIE_AGE = 60
# Will prrevent from logging you out after 60 seconds
# SESSION_SAVE_EVERY_REQUEST = True

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fleet_jxmtsi_repo',
        'USER': 'fleet',
        'PASSWORD': 'fleet',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'FLEET-index'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
}


django_heroku.settings(locals())

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'fmsconnected@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "frkytugornfqftas"

SESSION_ENGINE= 'django.contrib.sessions.backends.cached_db'
SESSION_TIMEOUT_REDIRECT = '/logout/'
# sSESSION_EXPIRE_SECONDS = 10
SESSION_COOKIE_AGE = 3600
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 3600
