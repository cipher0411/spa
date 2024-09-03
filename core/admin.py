# admin.py
from django.contrib import admin
from .models import Appointment
from .models import ContactMessage

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'service')
    search_fields = ('name', 'email', 'phone', 'service')
    list_filter = ('date', 'service')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject', 'message', 'phone')
    list_filter = ('sent_at',)

admin.site.register(ContactMessage, ContactMessageAdmin)