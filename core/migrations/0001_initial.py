# Generated by Django 5.1 on 2024-08-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('service', models.CharField(choices=[('massage', 'Massage'), ('facial', 'Facial'), ('manicure', 'Manicure'), ('pedicure', 'Pedicure')], max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
