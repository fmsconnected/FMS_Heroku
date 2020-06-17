from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.shortcuts import render,HttpResponseRedirect, get_list_or_404,HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from openpyxl import Workbook
import datetime
from datetime import date, timedelta
from .models import (
		Corrective,
)
from masterlist.models import (
    EmployeeMasterlist,
    VehicleMasterList,
    Leasing
    )
from django.views.generic import (
     DetailView,
     ListView,
     CreateView,
     UpdateView,
 )
# from django.views.generic.edit import (
    # DeleteView,
# )
# from . forms import (
#     carrequestform,
#     gascardform,
#     serviceform,
#     repairform,

#     )

from bootstrap_modal_forms.generic import (
                                           BSModalDeleteView
                                           )


                      #####################################  
                    #########################################
                   #####.     Vehicle Repair  Request    #####
                    #########################################
                     ######################################


class correctiveListView(ListView):
    model = Corrective
    template_name='corrective_list.html'
    
# def correctiveCreate(request):
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#     emplist = EmployeeMasterlist.objects.all()
#     vlist = VehicleMasterList.objects.all()
#     return render(request, 'corrective_form.html',{'Title':'Corrective - Corrective Maintenance','emplist':emplist,'vlist':vlist})

# def correctivesubmit(request):
#     if request.method == 'POST':
#         request_date = request.POST.get('request_date')
#         emp_id = request.POST.get('emp_id')
#         cost_center = request.POST.get('cost_center')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         c_no = request.POST.get('c_no')
#         company = request.POST.get('company')
#         department = request.POST.get('department')
#         group = request.POST.get('group')
#         plate_no = request.POST.get('plate_no')
#         v_brand = request.POST.get('v_brand')
#         engine = request.POST.get('engine')
#         v_model = request.POST.get('v_model')
#         v_make = request.POST.get('v_make')
#         chassis = request.POST.get('chassis')
#         v_band = request.POST.get('v_band')
#         cs_no = request.POST.get('cs_no')
#         eq_no = request.POST.get('eq_no')
#         fleet_area = request.POST.get('fleet_area')
#         particulars = request.POST.get('particulars')
#         category = request.POST.get('category')
#         maintenance_type1 = request.POST.get('maintenance_type1')
#         maintenance_type2 = request.POST.get('maintenance_type2')
#         scope_work1 = request.POST.get('scope_work1')
#         scope_work2 = request.POST.get('scope_work2')
#         recomendations = request.POST.get('recomendations')
#         service_reminder = request.POST.get('service_reminder')
#         repair_verified_by = request.POST.get('repair_verified_by')
#         work_order1 = request.POST.get('work_order1')
#         work_order2 = request.POST.get('work_order2')
#         work_order3 = request.POST.get('work_order3')
#         date_work_created = request.POST.get('date_work_created')
#         repair_shop = request.POST.get('repair_shop')
#         memo_app = request.POST.get('memo_app')
#         date_forward = request.POST.get('date_forward')
#         estimate_no = request.POST.get('estimate_no')
#         maintenance_amount = request.POST.get('maintenance_amount')
#         less_discount = request.POST.get('less_discount')
#         estimate_remark = request.POST.get('estimate_remark')
#         estimate_attach = request.POST.get('estimate_attach')
#         approved_by = request.POST.get('approved_by')
#         kilo_reading = request.POST.get('kilo_reading')
#         vrr_sla = request.POST.get('vrr_sla')

#         saveto_repair = Corrective(request_date=request_date, employee=emp_id, cost_center=cost_center, first_name=fname,
#             last_name=lname, contact_no=c_no, company=company, department=department, group_section=group,
#             plate_no=plate_no, v_brand=v_brand, engine=engine, v_make=v_make, v_model=v_model, chassis=chassis,
#             band=v_band, cond_sticker=cs_no, equipment_no=eq_no, fleet_area=fleet_area, particulars=particulars,
#             category=category, maintenance_type1=maintenance_type1, scope_work1=scope_work1, maintenance_type2=maintenance_type2,
#             scope_work2=scope_work2, recommendations=recomendations, service_reminder=service_reminder, verified_by=repair_verified_by,
#             work_order1=work_order1, work_order2=work_order2, work_order3=work_order3, datework_created=date_work_created,
#             Shop_vendor=repair_shop, date_forwarded=date_forward, estimate_no=estimate_no, maintenance_amount=maintenance_amount,
#             less_discount=less_discount, estimate_remarks=estimate_remark, estimate_attached=estimate_attach, approvedby=approved_by,
#             meter_reading=kilo_reading, VRR_SLA=vrr_sla, memo_app=memo_app,
#     )
#         saveto_repair.save()

#         return HttpResponseRedirect('/Corrective/Corrective/')

# class correctiveDetailView(DetailView):
#     model = Corrective
#     template_name = 'corrective_details.html'

# # class correctiveUpdateView(SuccessMessageMixin, UpdateView):
# #     model = Corrective
# #     form_class = repairform
# #     template_name = 'corrective_new.html'
    
# #     def get_success_message(self, cleaned_data):
# #     	print(cleaned_data)
# #     	return "Corrective Maintenance Updated Successfully!"

# class correctiveDeleteView(BSModalDeleteView):
#     model = Corrective
#     template_name = 'corrective_delete.html'
#     success_message = 'Success: Corrective Data was deleted.'
#     success_url = reverse_lazy('corrective_list')

# def correctiveHistoryView(request):
#     if request.method == "GET":
#        obj = Corrective.history.all()

#        return render(request, 'corrective_history.html', context={'object': obj})

