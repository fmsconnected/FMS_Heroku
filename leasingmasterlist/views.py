from django.shortcuts import render,HttpResponseRedirect,HttpResponse,reverse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import generic
import datetime
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
     ListView,
     CreateView,
     DetailView,
     UpdateView,
 )
from .models import Leasing
from . forms import (
    leasing_form
    )
from bootstrap_modal_forms.generic import BSModalDeleteView

from rest_framework import viewsets
from rest_framework.response import Response
# from .models import VehicleMasterList,
from .serializers import (
    leasingSerializer
    )

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

 #######################################  
##############  Leasing  ################
 #######################################


def leasing(request):
    return render(request, 'leasing_list.html')


class leasingViewSet(viewsets.ModelViewSet):
    queryset = Leasing.objects.all().order_by('id')
    serializer_class = leasingSerializer


class leasingCreateView(CreateView):
    model = Leasing
    form_class = leasing_form
    template_name = 'leasing_form.html'


class leasingUpdateView(UpdateView):
    model = Leasing
    form_class = leasing_form
    template_name = 'leasing_form.html'


class leasingDetailView(DetailView):
    model = Leasing
    template_name = 'leasing_details.html'


def leasingHistoryView(request):
    if request.method == "GET":
       obj = Leasing.history.all()

       return render(request, 'leasing_history.html', context={'object': obj})



