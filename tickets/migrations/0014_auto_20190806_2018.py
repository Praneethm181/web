# Generated by Django 2.2.4 on 2019-08-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_raffle_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raffle',
            name='active',
        ),
        migrations.AddField(
            model_name='raffle',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
