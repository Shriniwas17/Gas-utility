from django.contrib.auth.models import User
from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.username} - {self.type}"

