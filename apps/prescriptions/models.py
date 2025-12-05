from django.db import models
from django.contrib.auth.models import User
from apps.patients.models import Patient
from django.core.validators import MinValueValidator


class Prescription(models.Model):
    FREQUENCY_CHOICES = [
        ('once_daily', 'Once Daily'),
        ('twice_daily', 'Twice Daily'),
        ('thrice_daily', 'Thrice Daily'),
        ('four_times', 'Four Times Daily'),
        ('as_needed', 'As Needed'),
    ]
    
    DURATION_UNITS = [
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months'),
    ]

    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medicine_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100, help_text="e.g., 500mg, 10ml")
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    duration = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    duration_unit = models.CharField(max_length=10, choices=DURATION_UNITS)
    instructions = models.TextField(blank=True, null=True)
    side_effects = models.TextField(blank=True, null=True)
    prescribed_by = models.ForeignKey(User, on_delete=models.PROTECT)
    prescribed_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-prescribed_date']
        indexes = [
            models.Index(fields=['patient', '-prescribed_date']),
        ]

    def __str__(self):
        return f"{self.medicine_name} for {self.patient.full_name}"
