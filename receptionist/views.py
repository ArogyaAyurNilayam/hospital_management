from django.shortcuts import render, redirect
from django.http import HttpResponse
from Coordinator import views as coordinator_views
from Pharmacist import views as pharmacist_views
from Coordinator.models import User as CoordinatorUser
from Pharmacist.models import Medicine as PharmacistMedicine

from .models import PatientRegistration,Consultation_details
from .forms import PatientRegistrationForm
from datetime import datetime

# from .forms import AssignOPForm
# Create your views here.

def receptionist_homepage(request):
    return render(request, 'rechome.html')

def patient_registration_submit(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.op_number = generate_op_number()  # Generate OP number
            patient.save()
            return HttpResponse(f"<script>alert('Patient Successfully Added with OP Number: {patient.op_number}');window.location.href='/rhome/';</script>")
    else:
        form = PatientRegistrationForm()
    
    return render(request, 'ptreg.html', {'form': form})

def generate_op_number():
    from datetime import datetime
    current_date = datetime.now()
    year_month = current_date.strftime("%m%Y")  # Format month and year as 'MMYYYY'
    
    # Get the latest patient with the same year and month
    last_patient = PatientRegistration.objects.filter(op_number__startswith=year_month).last()
    
    if last_patient:
        # Extract the registration number part from the last OP number and increment it
        last_op_number = int(str(last_patient.op_number)[:2])
        reg_number = str(last_op_number + 1).zfill(2)  # Ensure the registration number is always 2 digits
    else:
        # First patient in the month, starting from 01
        reg_number = "01"
    
    # Return the generated OP number in the format YYYYMMDD
    op_number = reg_number +year_month 
    return op_number



def enter_op_number(request):
    if request.method == 'POST':
        op_number_value = request.POST.get('op_number')
        return redirect('assign_doctor', op_number=op_number_value)
    return render(request, 'op_number.html')
    



def assign_doctor(request, op_number):
    patient = PatientRegistration.objects.get(op_number=op_number)
    if request.method == 'POST':
        date = request.POST.get('date')
        formatted_date = datetime.strptime(date, "%Y-%m-%d").date()
        doctor_name = request.POST.get('doctor')
        
        consultation_details = Consultation_details.objects.create(
            op_number=op_number,
            patient_name=f"{patient.first_name} {patient.last_name}",
            date=formatted_date, doctor=doctor_name

        )
        consultation_details.save()
        return HttpResponse("<script>window.alert('Successfully Added Patient for consultation !!!!');window.location.href='/rhome/'</script>")
    else:
        all_doctors = CoordinatorUser.objects.filter(Designation='Doctor', is_approved=True)        
        return render(request, 'assign_doctor.html', {'op_number': op_number, 'patient': patient, 'all_doctors': all_doctors})


