from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required
from .forms import PatientForm

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'list.html',  {'patients': patients})

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patients/')
    else:
        form = PatientForm()
    return render(request, "patient_create.html", {'form': form})

@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.phone = request.POST.get('phone')
        patient.save()
        return redirect('/patients')
    return render(request, 'patient_edit.html', {'patient': patient})

@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('/patients')
from rest_framework.generics import ListCreateAPIView
from .serializers import PatientSerializer

class PatientListCreateAPI(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer