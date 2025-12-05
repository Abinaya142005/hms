from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Patient
from .forms import PatientForm, PatientSearchForm


@login_required(login_url='users:login')
def patient_list(request):
    patients = Patient.objects.all().order_by('-created_at')
    form = PatientSearchForm()
    
    search = request.GET.get('search', '')
    if search:
        patients = patients.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search)
        )
    
    paginator = Paginator(patients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'patients': page_obj.object_list,
        'form': form,
        'search': search,
    }
    
    return render(request, 'patients/patient_list.html', context)


@login_required(login_url='users:login')
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    prescriptions = patient.prescriptions.all()
    
    context = {
        'patient': patient,
        'prescriptions': prescriptions,
    }
    
    return render(request, 'patients/patient_detail.html', context)


@login_required(login_url='users:login')
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.created_by = request.user
            patient.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patients:patient-detail', patient_id=patient.patient_id)
    else:
        form = PatientForm()
    
    context = {'form': form, 'title': 'Add New Patient'}
    return render(request, 'patients/patient_form.html', context)


@login_required(login_url='users:login')
def patient_update(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patients:patient-detail', patient_id=patient.patient_id)
    else:
        form = PatientForm(instance=patient)
    
    context = {'form': form, 'patient': patient, 'title': 'Edit Patient'}
    return render(request, 'patients/patient_form.html', context)


@login_required(login_url='users:login')
@require_http_methods(["POST"])
def patient_delete(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully!')
    return redirect('patients:patient-list')
