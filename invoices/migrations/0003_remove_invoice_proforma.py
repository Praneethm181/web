# Generated by Django 2.2.3 on 2019-10-01 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20190729_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='proforma',
        ),
    ]
