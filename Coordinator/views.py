from django.shortcuts import render,redirect
from Home import views
from Pharmacist import views
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Coordinator.models import User
from Pharmacist.models import Medicine
from Coordinator import views
from .forms import MedicineForm
from receptionist.models import PatientRegistration,Consultation_details
# Create your views here.

@login_required
def admin_home(request):
    return render(request,'adminhome.html')

@login_required
def admin_regview(request):
    # Fetching staff details where is_approved is False and is not a superuser
    details = User.objects.filter(is_approved=False, is_superuser=False)
    return render(request, 'approvestaff.html', {'data': details})



@login_required
def admin_staffview(request):
    # Fetching staff details where is_approved is False and is not a superuser
    details1 = User.objects.filter(is_approved=True, is_superuser=False)
    return render(request, 'staffdetails.html', {'data1': details1})

@login_required
def admin_medview(request):
    # Fetching staff details where is_approved is False and is not a superuser
    details = Medicine.objects.filter(is_approved=False)
    return render(request, 'medicineupdates.html', {'data': details})

@login_required
def admin_approve_staff(request, staff_id):
   
    staff = User.objects.get(id=staff_id)

    staff.is_approved = 'True'
    staff.save()
    return HttpResponse("<script>window.alert('Successfully Approved!!!!');window.location.href='/approve/'</script>")



@login_required
def admin_reject_staff(request,staff_id):
   
    staff = User.objects.get(id=staff_id)
    staff.delete()
    return HttpResponse("<script>window.alert('Successfully Rejected the application!!!!');window.location.href='/approve/'</script>")

@login_required
def admin_medicineview(request):
    details2 = Medicine.objects.all()
    return render(request, 'medicinestock.html', {'data3': details2})



@login_required
def admin_approve_medicine(request, med_id):
   
    medicine = Medicine.objects.get(id=med_id)

    medicine.is_approved = 'True'
    medicine.save()
    return HttpResponse("<script>window.alert('Successfully Approved!!!!');window.location.href='/ap_re/'</script>")


@login_required
def admin_reject_medicine(request,med_id):
   
    medicine = Medicine.objects.get(id=med_id)
    medicine.delete()
    return HttpResponse("<script>window.alert('Successfully Rejected the application for medicine stock!!!!');window.location.href='/ap_re/'</script>")

@login_required
def admin_delete_medstock(request,med_id):
    medicine = Medicine.objects.get(id=med_id)
    medicine.delete()
    return HttpResponse("<script>window.alert('Successfully deleted the medicine record!!!!');window.location.href='/adminmedview/'</script>")

@login_required
def admin_edit_medicine(request, med_id):
    medicine = Medicine.objects.get(id=med_id)
    return render(request, 'medstock_update.html', {'data': medicine})

@login_required
def admin_update_medstock(request, med_id):
    medicine = Medicine.objects.get(id=med_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return HttpResponse("<script>window.alert('Successfully Updated !!!!');window.location.href='/adminmedview/'</script>")
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'admin_update_medstock.html', {'form': form, 'data': medicine})


@login_required
def patient_data(request):
    pt=PatientRegistration.objects.all
    return render(request, 'patient_data.html', {'patients': pt})


@login_required
def patient_delete(request,op_number):
    pt = PatientRegistration.objects.get(op_number=op_number)
    pt.delete()
    return HttpResponse("<script>window.alert('Successfully deleted the Patient record!!!!');window.location.href='/patient_data/'</script>")

@login_required
def patient_records(request):
    pt=Consultation_details.objects.all()
    return render(request, 'patient_records.html', {'patients': pt})
    
@login_required
def patient_consult_delete(request, op_number, date):
    pt = Consultation_details.objects.filter(op_number=op_number, date=date)
    pt.delete()
    return HttpResponse("<script>window.alert('Successfully deleted the Patient record!!!!');window.location.href='/patient_records/'</script>")