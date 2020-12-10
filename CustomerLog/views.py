from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import generic
import datetime
from datetime import date, timedelta
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


def CS_updateform(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    cclog = CS_log.objects.all()
    return render(request, 'CS/CS_update.html', {'title': 'Customer Care Log', 'cclog': cclog})


def cclog_alert(request):
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    dl2 = CS_log.objects.filter(
        Date_received__date=datetime.datetime.today() + timedelta(days=2))
    dl1 = CS_log.objects.filter(
        Date_received__date=datetime.datetime.today() + timedelta(days=1))
    dl = CS_log.objects.filter(
        Date_received__date=datetime.datetime.today())

    ccAlert = dl1.aggregate(counted=Count('id'))['counted'] + dl2.aggregate(counted=Count('id'))['counted'] + dl.aggregate(counted=Count('id'))[
        'counted']
    print(ccAlert)
    return render(request, 'CS/CS_list.html', {'title': 'CC log alert - Alert', 'ccAlert': ccAlert})


@user_passes_test(in_group)
def CSUpdate(request, pk):

    if request.method == 'POST':

        Date_received = request.POST.get('date_received')
        Fleet_member = request.POST.get('Fleet_member')
        Client_name = request.POST.get('Client_name')
        Email = request.POST.get('Email')
        Mobile_no = request.POST.get('Mobile_no')
        Transaction_type = request.POST.get('Transaction_type')
        Plate_no = request.POST.get('Plate_no')
        Problem = request.POST.get('Problem')
        Date_resolved = request.POST.get('Date_resolved')
        Action_taken = request.POST.get('Action_taken')

        d1 = datetime.datetime.strptime(Date_received, '%Y-%m-%d').date()
        d2 = datetime.datetime.strptime(Date_resolved, '%Y-%m-%d').date()
        ageing = (d2 - d1)

        CS_log.objects.filter(id=pk).update(Date_received=Date_received, Fleet_member=Fleet_member, Client_name=Client_name,
                                            Email=Email, Mobile_no=Mobile_no, Transaction_type=Transaction_type, Plate_no=Plate_no, Problem=Problem,
                                            Date_resolved=Date_resolved, Action_taken=Action_taken, Ageing=ageing)
    return HttpResponseRedirect('/Customer/')


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
