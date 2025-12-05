from django.contrib import admin
from .models import Prescription


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['prescription_id', 'medicine_name', 'patient', 'prescribed_date', 'frequency']
    list_filter = ['frequency', 'prescribed_date']
    search_fields = ['medicine_name', 'patient__first_name', 'patient__last_name']
    readonly_fields = ['prescription_id', 'prescribed_date', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Prescription Details', {
            'fields': ('patient', 'medicine_name', 'dosage', 'frequency', 'duration', 'duration_unit')
        }),
        ('Additional Information', {
            'fields': ('instructions', 'side_effects', 'notes')
        }),
        ('Metadata', {
            'fields': ('prescription_id', 'prescribed_by', 'prescribed_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
