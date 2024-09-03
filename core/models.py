from django.db import models


class Appointment(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('home', 'Home Service'),
        ('office', 'Office Visit'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=255)
    address = models.CharField(max_length=500, blank=True, null=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES, default='office')
    notes = models.TextField(blank=True, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment by {self.name} on {self.date} at {self.time}"



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"