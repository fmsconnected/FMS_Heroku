from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import generic
from django.core import serializers
import datetime
from django.utils import formats
from datetime import date, timedelta
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Q, Count
from bootstrap_modal_forms.generic import BSModalDeleteView
# User
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
)

from . forms import (
    fleet_card_form
)

from .serializers import (
    fleet_card_serializer
)
from .models import (
    fleet_card
)

class fleet_card_list(ListView):
    model = fleet_card
    template_name = 'fcm_list.html'

class fleet_card_create(CreateView):
    model = fleet_card
    form_class = fleet_card_form
    template_name = 'fcm_create.html'

class fleet_card_update(UpdateView):
    model = fleet_card
    form_class = fleet_card_form
    template_name = 'fcm_create.html'
    
class fleet_card_delete(BSModalDeleteView):
    model = fleet_card
    template_name = 'fcm_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('Fcm_list')


def fcm_export(request):
    fcm_queryset = fleet_card.objects.all()
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=Fleet Card Monitoring.xlsx'
    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = 'Fleet Card Monitoring'

    columns = [
        'STATUS',
        'RECEIVED_REQUEST',
        'DATE_VERIFIED',
        'DATE_RECEIVED',
        'DATE_ISSUED',
        'WORK_DAYS',
        'CARD_NUMBER', 
        'NAME',
        'COST_CENTER',
        'PLATE_NUMBER',
        'CARD_TYPE',
        'CABONILLA',
        'STATION'
    ]
    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for fcm in fcm_queryset:
        row_num += 1
        row = [
            fcm.STATUS,
            fcm.RECEIVED_REQUEST,
            fcm.DATE_VERIFIED,
            fcm.DATE_RECEIVED,
            fcm.DATE_ISSUED,
            fcm.WORK_DAYS,
            fcm.CARD_NUMBER, 
            fcm.NAME,
            fcm.COST_CENTER,
            fcm.PLATE_NUMBER,
            fcm.CARD_TYPE,
            fcm.CABONILLA,
            fcm.STATION
        ]

        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response






