from django.shortcuts import render,HttpResponseRedirect,HttpResponse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from openpyxl.styles.colors import Color
import datetime
from datetime import date, timedelta
from django.urls import reverse_lazy

from .serializers import (
    shell_report_Serializer
    )
from . models import shell_report
from rest_framework import viewsets
from django.views.generic import (
                				CreateView,
                				ListView,
                				UpdateView,
                				DetailView,
                				)
from django.db.models import Sum


def monthly_report_shell(request):
	return render(request, 'shell/shell_list.html')

class shell_report_ViewSet(viewsets.ModelViewSet):
    queryset = shell_report.objects.all().order_by('id')
    serializer_class = shell_report_Serializer

class monthly_report_shellDetails(DetailView):
    model = shell_report
    template_name = 'shell/shell_details.html'
