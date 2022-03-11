from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from django.db.models import DateTimeField


class MytypeField(DateTimeField):
    def db_type(self, connection):
        return 'date'


def increment_Activity_id():
    last_in = CS_log.objects.all().order_by('id').last()
    if not last_in:
        return 'CC' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
    in_id = last_in.Activity_id
    in_int = int(in_id[10:])
    new_in_int = in_int + 1
    new_in_id = 'CC' + str(datetime.datetime.today().strftime('%Y')) + \
        '-' + str(new_in_int).zfill(6)
    return new_in_id


class CS_log(models.Model):

    member = (
        ('Shane Santos', 'Shane Santos'),
        ('Francis Dela Cruz', 'Francis Dela Cruz'),
        ('Glaiza Cabillo', 'Glaiza Cabillo'),
        ('Janine Manzo', 'Janine Manzo'),
        ('Jessie Blanquisco', 'Jessie Blanquisco'),
        ('Maribel Evaristo', 'Maribel Evaristo'),
        ('Princess Concepsion', 'Princess Concepsion'),
        ('Stephanie Warde', 'Stephanie Warde'),
        ('Dennis Alonzo', 'Dennis Alonzo'),
        ('Jerald Perez', 'Jerald Perez'),
    )

    trans_type = (
        ('Accident Report', 'Accident Report'),
        ('Billing', 'Billing'),
        ('Car Rental', 'Car Rental'),
        ('Fleet Card', 'Fleet Card'),
        ('Insurance', 'Insurance'),
        ('Plate Number', 'Plate Number'),
        ('Vehicle Acquisition', 'Vehicle Acquisition'),
        ('Vehicle Disposal', 'Vehicle Disposal'),
        ('Vehicle Leasing', 'Vehicle Leasing'),
        ('Vehicle Registration', 'Vehicle Registration'),
        ('Others', 'Others'),
    )

    Activity_id = models.CharField(
        max_length=100, default=increment_Activity_id)
    Date_received = MytypeField()
    Fleet_member = models.CharField(
        max_length=100, blank=True, null=True, choices=member)
    Ageing = models.CharField(max_length=100, blank=True,)
    Client_name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Mobile_no = models.CharField(max_length=100, blank=True, null=True)
    Transaction_type = models.CharField(
        max_length=100, blank=True, null=True, choices=trans_type)
    Plate_no = models.CharField(max_length=100, blank=True, null=True)
    Problem = models.CharField(
        max_length=100, blank=True, null=True)
    Date_resolved = models.CharField(max_length=100, blank=True)
    Date_resolved_inital = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    Action_taken = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.Activity_id

    def get_absolute_url(self):
        return reverse('CS_List')

    # def save(self, *args, **kwargs):
    #     self.Date_received = self.Date_received.replace(tzinfo=None)
    #     super(CS_log, self).save(*args, **kwargs)
