# from django.shortcuts import render

# # Create your views here.
# from django.views import generic
# from django.shortcuts import render,HttpResponseRedirect, get_list_or_404,HttpResponse
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy
# from openpyxl import Workbook
# import datetime
# from datetime import date, timedelta
# from .models import (
# 		CarRentalRequest,
#         Gas_card,
#         service_vehicle,
#         Vehicle_Repair,
# )
# from masterlist.models import (
#     EmployeeMasterlist,
#     VehicleMasterList,
#     Leasing
#     )
# from django.views.generic import (
#      DetailView,
#      ListView,
#      CreateView,
#      UpdateView,
#  )
# # from django.views.generic.edit import (
#     # DeleteView,
# # )
# from . forms import (
#     carrequestform,
#     gascardform,
#     serviceform,
#     repairform,

#     )

# from bootstrap_modal_forms.generic import (
#                                            BSModalDeleteView
#                                            )


#                       #####################################  
#                     #########################################
#                    #####.     Vehicle Repair  Request    #####
#                     #########################################
#                      ######################################


# class repairListView(ListView):
#     model = Vehicle_Repair
#     template_name='vehicle_repair/repair_list.html'
    
# def repairCreate(request):
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#     emplist = EmployeeMasterlist.objects.all()
#     vlist = VehicleMasterList.objects.all()
#     return render(request, 'vehicle_repair/repair_new.html',{'Title':'Vehicle - Vehicle Repair','emplist':emplist,'vlist':vlist})

# def repairsubmit(request):
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

#         saveto_repair = Vehicle_Repair(request_date=request_date, employee=emp_id, cost_center=cost_center, first_name=fname,
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

#         return HttpResponseRedirect('/Request/Repair/')

# class repairDetailView(DetailView):
#     model = Vehicle_Repair
#     template_name = 'vehicle_repair/repair_details.html'

# class repairUpdateView(SuccessMessageMixin, UpdateView):
#     model = Vehicle_Repair
#     form_class = repairform
#     template_name = 'vehicle_repair/repair_form.html'
    
#     def get_success_message(self, cleaned_data):
#     	print(cleaned_data)
#     	return "Vehicle Repair Request Updated Successfully!"

# class repairDeleteView(BSModalDeleteView):
#     model = Vehicle_Repair
#     template_name = 'vehicle_repair/repair_delete.html'
#     success_message = 'Success: Vehicle Repair Request was deleted.'
#     success_url = reverse_lazy('repair_list')

# def repairHistoryView(request):
#     if request.method == "GET":
#        obj = Vehicle_Repair.history.all()

#        return render(request, 'vehicle_repair/repair_history.html', context={'object': obj})


# def repair_request_excel(request):
#     repair_queryset = Vehicle_Repair.objects.all()   
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#     )
#     response['Content-Disposition'] = 'attachment; filename=Vehicle Repair Request.xlsx'
#     workbook = Workbook()

#     worksheet = workbook.active
#     worksheet.title = 'Vehicle Repair Request'

#     columns = [
#                 'Request Date' ,
#                 'Employee' ,
#                 'Cost Center' ,
#                 'First Name' ,
#                 'Last Name' ,
#                 'Contact No' ,
#                 'Company' ,
#                 'Department' ,
#                 'Group Section' ,
#                 'Plate No' ,
#                 'Brand' ,
#                 'Engine' ,
#                 'Make' ,
#                 'Model' ,
#                 'Chassis' ,
#                 'Band' ,
#                 'Conduction Sticker' ,
#                 'Equipment No' ,
#                 'Fleet Area' ,
#                 'Particulars' ,
#                 'Category' ,
#                 'Maintenance Type 1' ,
#                 'Scope Work 1' ,
#                 'Maintenance Type 2' ,
#                 'Scope Work 2' ,
#                 'Recommendations' ,
#                 'Service Reminder' ,
#                 'Verified By' ,
#                 'Work Order 1' ,
#                 'Work Order 2' ,
#                 'Work Order 3' ,
#                 'Date Work Created' ,
#                 'Shop Vendor' ,
#                 'Memo App Number'
#                 'Date Forwarded' ,
#                 'Estimate No' ,
#                 'Maintenance Amount' ,
#                 'Less Discount' ,
#                 'Estimate Remarks' ,
#                 'Estimate Attached' ,
#                 'Approved By' ,
#                 'Meter Reading' ,
#                 'SLA' ,
#                 'Date Initiated' ,
#                 'Deadline',

#     ]
#     row_num = 1

#     for col_num, column_title in enumerate(columns, 1):
#         cell = worksheet.cell(row=row_num, column=col_num)
#         cell.value = column_title

#     for repair in repair_queryset:
#         row_num += 1
#         row = [
#                 repair.request_date,
#                 repair.employee ,
#                 repair.cost_center ,
#                 repair.first_name ,
#                 repair.last_name ,
#                 repair.contact_no ,
#                 repair.company ,
#                 repair.department ,
#                 repair.group_section ,
#                 repair.plate_no ,
#                 repair.v_brand ,
#                 repair.engine ,
#                 repair.v_make ,
#                 repair.v_model ,
#                 repair.chassis ,
#                 repair.band ,
#                 repair.cond_sticker ,
#                 repair.equipment_no ,
#                 repair.fleet_area ,
#                 repair.particulars ,
#                 repair.category ,
#                 repair.maintenance_type1 ,
#                 repair.scope_work1 ,
#                 repair.maintenance_type2 ,
#                 repair.scope_work2 ,
#                 repair.recommendations ,
#                 repair.service_reminder ,
#                 repair.verified_by ,
#                 repair.work_order1 ,
#                 repair.work_order2 ,
#                 repair.work_order3 ,
#                 repair.datework_created ,
#                 repair.Shop_vendor ,
#                 repair.memo_app,
#                 repair.date_forwarded ,
#                 repair.estimate_no ,
#                 repair.maintenance_amount ,
#                 repair.less_discount ,
#                 repair.estimate_remarks ,
#                 repair.estimate_attached ,
#                 repair.approvedby ,
#                 repair.meter_reading ,
#                 repair.VRR_SLA ,
#                 repair.date_initiated ,
#                 repair.Deadline,
#         ]
        
#         for col_num, cell_value in enumerate(row, 1):
#             cell = worksheet.cell(row=row_num, column=col_num)
#             cell.value = cell_value

#     workbook.save(response)
#     return response

