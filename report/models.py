from django.db import models
from django.urls import reverse
import datetime
from datetime import date,timedelta
from masterlist.models import EmployeeMasterlist,VehicleMasterList
# History
from simple_history.models import HistoricalRecords

def increment_Activity_id():
	last_in = vehicle_report.objects.all().order_by('id').last()
	if not last_in:
		return 'MVAR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'MVAR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class vehicle_report(models.Model):

    Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
    received_date = models.DateField(auto_now=False, blank=True, null=True)
    v_accident_type = models.CharField(max_length=100, blank=True, null=True)
    support_docs = models.CharField(max_length=100, blank=True, null=True)
    # plate_number = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
    plate_number = models.CharField(max_length=100, blank=True, null=True)
    v_model = models.CharField(max_length=100, blank=True, null=True)
    v_make = models.CharField(max_length=100, blank=True, null=True)
    cond_sticker = models.CharField(max_length=100, blank=True, null=True)
    # a_employee_id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING)
    a_employee_id = models.CharField(max_length=100, blank=True, null=True)
    a_employee_fname = models.CharField(max_length=100, blank=True, null=True)
    a_employee_lname = models.CharField(max_length=100, blank=True, null=True)
    a_employee_no = models.CharField(max_length=100, blank=True, null=True)
    a_employee_company = models.CharField(max_length=100, blank=True, null=True)
    a_employee_group = models.CharField(max_length=100, blank=True, null=True)
    a_employee_division = models.CharField(max_length=100, blank=True, null=True)
    a_employee_dept = models.CharField(max_length=100, blank=True, null=True)
    sup_employee_id = models.CharField(max_length=100, blank=True, null=True)
    sup_employee_fname = models.CharField(max_length=100, blank=True, null=True)
    sup_employee_lname = models.CharField(max_length=100, blank=True, null=True)
    inform_assignee = models.CharField(max_length=100, blank=True, null=True)
    date_of_inspection = models.CharField(max_length=100, blank=True, null=True)
    inspection_remarks = models.CharField(max_length=100, blank=True, null=True)
    date_filed_alarm = models.CharField(max_length=100, blank=True, null=True)
    date_cert_received = models.CharField(max_length=100, blank=True, null=True)
    date_forwarded = models.CharField(max_length=100, blank=True, null=True)
    date_initiated = models.DateField(auto_now=True, null=True)
    MVAR_SLA = models.CharField(max_length=10, null=True)
    history = HistoricalRecords()
    Deadline = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.Deadline is None:
            now = datetime.datetime.today()
            num_days = 0
            while num_days < 5:
                now = now + timedelta(days=1)
                if now.isoweekday() not in [6,7]:
                    num_days+=1
            self.Deadline = now
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Activity_id

    def get_absolute_url(self):
        return reverse('report_list')




    