# Generated by Django 5.1 on 2024-08-31 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_appointment_name_alter_appointment_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('massage', 'Massage'), ('facial', 'Facial'), ('manicure', 'Manicure'), ('pedicure', 'Pedicure')], max_length=100),
        ),
    ]
