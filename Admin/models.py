
from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


class UserReport(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.date)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.date, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.date, self.ip)
    class Meta:
        ordering = ('-date', )

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    UserReport.objects.create(action='user_logged_in',
                              ip=ip, username=user.username)


# @receiver(user_logged_out)
# def user_logged_out_callback(sender, request, user, **kwargs):
#     ip = request.META.get('REMOTE_ADDR')
#     UserReport.objects.create(action='user_logged_out',
#                               ip=ip, username=user.username)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    UserReport.objects.create(
        action='user_login_failed', username=credentials.get('username', None))

####### Customer care log ###########
