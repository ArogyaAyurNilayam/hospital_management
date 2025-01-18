from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Coordinator.models import User
from Coordinator import views
from Pharmacist import views
from Doctor import views

# Create your views here.


def home_page(request):
    return render(request,'index.html')

def reg_page(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        Designation=request.POST.get('designation')
        Email=request.POST.get('email')
        Phone=request.POST.get('phone')
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        
        s=User.objects.create_user(first_name=Name,Designation=Designation,email=Email,username=Username,phone=Phone,password=Password)
        s.save()
        return HttpResponse("<script>window.alert('Successfully Registered !!!!');window.location.href='/my/'</script>")
    else:
        return render(request,'regstaff.html')





def sign_in(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        stu=authenticate(request,username=uname,password=psw)
        if stu is not None:
            login(request,stu)
            if stu.is_superuser:
                return redirect("admin_home")

            elif stu.is_approved==1 and stu.Designation =='Pharmacist':
                request.session['t_id']=stu.id 
                return HttpResponse("<script>window.alert('Successfully Logged in !!!!');window.location.href='/phome/'</script>")

            elif stu.is_approved==1 and stu.Designation =='Receptionist':
                request.session['t_id']=stu.id 
                return HttpResponse("<script>window.alert('Successfully Logged in !!!!');window.location.href='/rhome/'</script>")

            elif stu.is_approved==1 and stu.Designation =='Doctor':
                request.session['t_id']=stu.id 
                return HttpResponse("<script>window.alert('Successfully Logged in !!!!');window.location.href='/dhome/'</script>")
                
                
        else:
            return HttpResponse("<script>window.alert('Invalid Username and Password !!!!');window.location.href='/lg/'</script>")


    else:
        return render(request,'logins.html')
