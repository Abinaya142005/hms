from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Prescription
from .forms import PrescriptionForm
from apps.patients.models import Patient


@login_required(login_url='users:login')
def prescription_list(request):
    prescriptions = Prescription.objects.all().order_by('-prescribed_date')
    
    context = {
        'prescriptions': prescriptions,
    }
    
    return render(request, 'prescriptions/prescription_list.html', context)


@login_required(login_url='users:login')
def prescription_detail(request, prescription_id):
    prescription = get_object_or_404(Prescription, prescription_id=prescription_id)
    
    context = {
        'prescription': prescription,
    }
    
    return render(request, 'prescriptions/prescription_detail.html', context)


@login_required(login_url='users:login')
def prescription_create(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.patient = patient
            prescription.prescribed_by = request.user
            prescription.save()
            messages.success(request, 'Prescription added successfully!')
            return redirect('patients:patient-detail', patient_id=patient.patient_id)
    else:
        form = PrescriptionForm()
    
    context = {
        'form': form,
        'patient': patient,
        'title': 'Add Prescription',
    }
    
    return render(request, 'prescriptions/prescription_form.html', context)


@login_required(login_url='users:login')
def prescription_update(request, prescription_id):
    prescription = get_object_or_404(Prescription, prescription_id=prescription_id)
    
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prescription updated successfully!')
            return redirect('patients:patient-detail', patient_id=prescription.patient.patient_id)
    else:
        form = PrescriptionForm(instance=prescription)
    
    context = {
        'form': form,
        'prescription': prescription,
        'patient': prescription.patient,
        'title': 'Edit Prescription',
    }
    
    return render(request, 'prescriptions/prescription_form.html', context)


@login_required(login_url='users:login')
@require_http_methods(["POST"])
def prescription_delete(request, prescription_id):
    prescription = get_object_or_404(Prescription, prescription_id=prescription_id)
    patient_id = prescription.patient.patient_id
    prescription.delete()
    messages.success(request, 'Prescription deleted successfully!')
    return redirect('patients:patient-detail', patient_id=patient_id)
