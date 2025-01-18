from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from Coordinator import views as coordinator_views
from Pharmacist import views as pharmacist_views
from Coordinator.models import User as CoordinatorUser
from Pharmacist.models import Medicine as PharmacistMedicine
from receptionist.models import Consultation_details
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Pharmacist.models import Bill_details
import json
from datetime import datetime


@login_required
def pharmacy_homepage(request):
    return render(request, 'homepage.html')


@login_required
def add_medicine(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        category = request.POST.get('Category')
        company = request.POST.get('Company')
        rate = request.POST.get('Rate')
        quantity = request.POST.get('Quantity')
        number = request.POST.get('Number')
        limit = request.POST.get('Limit')
        
        m = PharmacistMedicine.objects.create(Name=name, Category=category, Company=company, Rate=rate, Quantity=quantity, Number=number ,Limit=limit)
        m.save()
        return HttpResponse("<script>window.alert('Medicine Successfully Added !!!!');window.location.href='/medadd/'</script>")
    else:
        return render(request, 'addmedicine.html')


@login_required
def pharmacisit_medicineview(request):
    details2 = PharmacistMedicine.objects.filter(is_approved=True)
    return render(request, 'medstock.html', {'data3': details2})

@login_required
def search_prescription(request):
    return render(request,'prescription_search.html')

@login_required
def prescription_details(request):
    if request.method == 'GET':
        op_number = request.GET.get('op_number')
        date = request.GET.get('date')
        try:
            prescription_details = Consultation_details.objects.get(op_number=op_number, date=date)
            prescription_details.prescription = json.loads(prescription_details.prescription)

            return render(request, 'prescription_details.html', {'prescription_details': prescription_details})
        except Consultation_details.DoesNotExist:
            return HttpResponse("<script>alert('No patient record found !!!!');window.location.href='/search_prescription/';</script>")
        
    return render(request, 'prescription_search.html')


@login_required
def get_medicine_details(request):
    if request.method == 'GET' and request.is_ajax():
        medicine_id = request.GET.get('medicine_id')
        medicine = PharmacistMedicine.objects.get(pk=medicine_id)
        data = {
            'category': medicine.Category,
            'price': medicine.Rate
        }
        return JsonResponse(data)



# @login_required
# def billing(request):
#     op_number = request.GET.get('opNumber')
#     op_date_str = request.GET.get('opDate')
#     op_date = datetime.strptime(op_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    
#     bill_details = Bill_details.objects.filter(op_number=op_number, date=op_date)
#     print("Bill Details:", bill_details)  # Debugging line



#     total_amount_to_be_paid = sum([bill.total for bill in bill_details])
    
#     medicines = PharmacistMedicine.objects.all()  # Fetch all medicines from the database
    
#     context = {
#         'op_number': op_number,
#         'op_date': op_date,
#         'bill_details': bill_details if bill_details else [],
#         'total_amount_to_be_paid': total_amount_to_be_paid,
#         'medicines': medicines,
#     }

#     return render(request, 'gen.html', context)

@login_required
def billing(request):
    op_number = request.GET.get('opNumber')
    op_date_str = request.GET.get('opDate')

    # Try different date formats and handle errors
    try:
        # Attempt to parse full month name format: 'January 4, 2025'
        op_date = datetime.strptime(op_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        try:
            # Attempt to parse abbreviated month name format: 'Jan. 4, 2025'
            op_date = datetime.strptime(op_date_str, '%b. %d, %Y').strftime('%Y-%m-%d')
        except ValueError:
            # If both parsing attempts fail, fall back to the original string (or handle the error appropriately)
            op_date = None  # Or raise an error if needed

    # Fetch bill details if op_date is valid
    if op_date:
        bill_details = Bill_details.objects.filter(op_number=op_number, date=op_date)
        total_amount_to_be_paid = sum([bill.total for bill in bill_details])
    else:
        bill_details = []
        total_amount_to_be_paid = 0
    
    # Fetch medicines list
    medicines = PharmacistMedicine.objects.all()
    
    # Prepare context
    context = {
        'op_number': op_number,
        'op_date': op_date,
        'bill_details': bill_details if bill_details else [],
        'total_amount_to_be_paid': total_amount_to_be_paid,
        'medicines': medicines,
    }

    # Return response with context
    return render(request, 'gen.html', context)



@login_required

def save_bill(request):
    if request.method == 'POST':
        op_number = request.POST.get('op_number')
        date = request.POST.get('date')
        print(date)
        # op_date = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
        medicine_id = request.POST.get('medicine_name')
        medicine = PharmacistMedicine.objects.get(id=medicine_id)
        medicine_name = medicine.Name
        rate = request.POST.get('rate')
        quantity = request.POST.get('quantity')
        total = int(rate) * int(quantity)

        medicine.Number-= int(quantity)
        medicine.save()
        
        # Save data to the database
        bill = Bill_details(
            op_number=op_number,
            date=date,
            medicine_name=medicine_name,
            rate=rate,
            quantity=quantity,
            total=total
        )
        bill.save()
        
        # Fetch bill details after saving
        bill_details = Bill_details.objects.filter(op_number=op_number, date=date)
        total_amount_to_be_paid = sum([bill.total for bill in bill_details])
    
        medicines = PharmacistMedicine.objects.all()
        context = {
            'op_number': op_number,
            'op_date': date,
            'bill_details': bill_details if bill_details else [],
            'total_amount_to_be_paid': total_amount_to_be_paid,
            'medicines': medicines,
        }
        
        # Redirect back to billing page
        return render(request, 'gen.html', context)

    return render(request, 'gen.html')





@login_required
def delete_bill(request, mid):
    bill_details = get_object_or_404(Bill_details, id=mid)
    quantity = bill_details.quantity
    op_number = bill_details.op_number
    op_date = bill_details.date
    print(op_date)
    if not isinstance(op_date, str):
        op_date = op_date.strftime('%Y-%m-%d')
    



    medicine_name = bill_details.medicine_name
    medicine = PharmacistMedicine.objects.get(Name=medicine_name)
    medicine.Number += quantity  # Increment the quantity
    medicine.save()

    bill_details.delete()

    bill_details = Bill_details.objects.filter(op_number=op_number, date=op_date)
    total_amount_to_be_paid = sum([bill.total for bill in bill_details])
    
    medicines = PharmacistMedicine.objects.all()
    
    context = {
        'op_number': op_number,
        'op_date': op_date,
        'bill_details': bill_details if bill_details else [],
        'total_amount_to_be_paid': total_amount_to_be_paid,
        'medicines': medicines,
    }

    return render(request, 'gen.html', context)


@login_required
def edit_bill(request,mid):
    print('.......',mid)
    med=Bill_details.objects.get(id=mid)
    op_number=med.op_number
    op_date=med.date
    medicines = PharmacistMedicine.objects.all()
    bill_details = Bill_details.objects.filter(op_number=op_number, date=op_date).exclude(id=mid)
   
    return render(request,'gen_up.html',{'data':med, 'medicines': medicines,'bill_details': bill_details})




def update_bill(request, mid):
    if request.method == 'POST':
        med = Bill_details.objects.get(id=mid)
        op_number=med.op_number
        op_date=med.date
        quant=med.quantity
        medicine_name = request.POST.get('medicine_name')
        quantity = request.POST.get('quantity')
        rate = request.POST.get('rate')
        
        # Retrieve the medicine object corresponding to the selected medicine name
        medicine = PharmacistMedicine.objects.get(Name=medicine_name)
        medicine.Number += quant
        medicine.save()
        medicine.Number-=int(quantity)
        medicine.save()
        
        # Update the current bill detail
        med.medicine_name= medicine.Name
        med.quantity = quantity
        med.rate = rate
        med.total = int(rate) * int(quantity)
        med.save()



        bill_details = Bill_details.objects.filter(op_number=op_number, date=op_date)
    
        medicines = PharmacistMedicine.objects.all()
    
        context = {
        'op_number': op_number,
        'op_date': op_date,
        'bill_details': bill_details if bill_details else [],
        'medicines': medicines,
        }

        return render(request, 'gen.html', context)
        
        
def see_bill(request):
    op_number = request.GET.get('opNumber')
    op_date_str = request.GET.get('opDate')
    
    try:
        op_date = datetime.strptime(op_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        op_date = op_date_str
    
    bill_details = Bill_details.objects.filter(op_number=op_number, date=op_date)
    total_amount = sum(detail.total for detail in bill_details)
    total_amount = sum(detail.total for detail in bill_details)
    return render(request, 'see_bill.html', {'bill_details': bill_details, 'op_number': op_number, 'op_date': op_date,'total_amount':total_amount})



def proceed_bill(request):
    op_number = request.GET.get('opNumber')
    op_date_str = request.GET.get('opDate')
    total_amount=request.GET.get('total_amount')
    try:
        op_date = datetime.strptime(op_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        op_date = op_date_str

    item= Consultation_details.objects.get(op_number=op_number, date=op_date)
    item.bill_amount=total_amount
    item.save()
    return HttpResponse("<script>alert('Payment Successful !!!!');window.location.href='/phome/';</script>")






        
    


    





@login_required
def logouts(request):
    logout(request)
    # return redirect(sign_in)
    return HttpResponse("<script>window.alert('Successfully Logged out!!!!');window.location.href='/lg/'</script>")







