from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')

