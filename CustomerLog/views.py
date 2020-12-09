from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import generic
import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalDeleteView

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
)

from . forms import (
    CS_form
)

from .serializers import (
    CS_log_serializer
)
from .models import (
    CS_log
)


class CSCreateView(CreateView):
    model = CS_log
    form_class = CS_form
    template_name = 'CS/CS_create.html'


# class FuelCreateView(SuccessMessageMixin, CreateView):
#     model = Fuel_supplier
#     form_class = FuelsupplierForm
#     template_name = 'payment/fuel/fuel_supplier.html'

#     def get_success_message(self, cleaned_data):
#         print(cleaned_data)
#         return "Fuel Supplier Has been Created!"


class CSListView(ListView):
    model = CS_log
    template_name = 'CS/CS_list.html'


class CSDetails(DetailView):
    model = CS_log
    template_name = 'CS/CS_details.html'


class CSUpdate(UpdateView):
    model = CS_log
    form_class = CS_form
    template_name = 'CS/CS_update.html'


class CSDeleteView(BSModalDeleteView):
    model = CS_log
    template_name = 'CS/CS_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('CS_List')
