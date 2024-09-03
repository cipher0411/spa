# Generated by Django 5.1 on 2024-09-01 00:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_appointment_name_alter_appointment_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='requested_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(max_length=255),
        ),
    ]
