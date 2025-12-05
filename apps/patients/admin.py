from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'full_name', 'email', 'phone', 'created_at']
    list_filter = ['gender', 'blood_group', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['patient_id', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone')
        }),
        ('Medical Information', {
            'fields': ('blood_group', 'allergies', 'medical_history')
        }),
        ('Contact Information', {
            'fields': ('address', 'city', 'state', 'postal_code', 'emergency_contact')
        }),
        ('Metadata', {
            'fields': ('patient_id', 'created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
