from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import generic
import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
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
    CS_form,
    CS_formupdate
)

from .serializers import (
    CS_log_serializer
)
from .models import (
    CS_log
)


def in_group(user):
    if user.groups.filter(name="CustomerLog").exists():
        return True
    else:
        raise PermissionDenied


class CSCreateView(CreateView):
    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = CS_log
    form_class = CS_form
    template_name = 'CS/CS_create.html'


class CSListView(ListView):
    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = CS_log
    template_name = 'CS/CS_list.html'


class CSDetails(DetailView):
    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = CS_log
    template_name = 'CS/CS_details.html'


class CSUpdate(UpdateView):
    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = CS_log
    form_class = CS_formupdate
    template_name = 'CS/CS_update.html'


class CSDeleteView(BSModalDeleteView):
    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = CS_log
    template_name = 'CS/CS_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('CS_List')


@user_passes_test(in_group)
def customer_log_excel(request):
    customer_queryset = CS_log.objects.all()
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=Customer Care Log.xlsx'
    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = 'Customer Care Log'

    columns = [
        'Ticket Number',
        'Date Received',
        'Fleet Member',
        'Client Name',
        'Email',
        'Mobile Number',
        'Transaction Type',
        'Plate Number',
        'Problem',
        'Date Resolved',
        'Action Taken'
    ]
    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for cc in customer_queryset:
        row_num += 1
        row = [
            cc.Activity_id,
            cc.Date_received,
            cc.Fleet_member,
            cc.Client_name,
            cc.Email,
            cc.Mobile_no,
            cc.Transaction_type,
            cc.Plate_no,
            cc.Problem,
            cc.Date_resolved,
            cc.Action_taken
        ]

        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response
