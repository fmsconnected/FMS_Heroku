# Generated by Django 2.1.7 on 2020-11-11 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20201111_1403'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuditEntry',
            new_name='UserReport',
        ),
    ]