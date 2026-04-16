from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient


@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'app_list.html', {'appointments': appointments})


@login_required
def appointment_create(request):
    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        patient_id = request.POST.get('patient')

        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)

        Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_time=request.POST.get('appointment_time'),
            appointment_status=request.POST.get('appointment_status')
        )

        return redirect('/appointments')

    return render(request, 'appointment_create.html', {
        'doctors': Doctor.objects.all(),
        'patients': Patient.objects.all()
    })


@login_required
def appointment_edit(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        patient_id = request.POST.get('patient')

        appointment.doctor = Doctor.objects.get(id=doctor_id)
        appointment.patient = Patient.objects.get(id=patient_id)
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.appointment_status = request.POST.get('appointment_status')

        appointment.save()
        return redirect('/appointments')

    return render(request, 'appointment_edit.html', {
        'appointment': appointment,
        'doctors': Doctor.objects.all(),
        'patients': Patient.objects.all()
    })


@login_required
def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('/appointments')