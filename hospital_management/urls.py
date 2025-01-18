"""
URL configuration for hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views as home_views
from Coordinator import views as coordinator_views
from Pharmacist import views as pharmacist_views
from receptionist import views as receptionist_views
from Doctor import views as doctor_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path("my/", home_views.home_page),
    path("lg/", home_views.sign_in, name='signin'),
    path("adminhome/", coordinator_views.admin_home, name='admin_home'),
    path("adminstaff/", coordinator_views.admin_staffview, name='admin_staffview'),
    path("reg/", home_views.reg_page, name='registration'),
    path("approve/", coordinator_views.admin_regview,name='approve_reject'),
    path("ap_re/", coordinator_views.admin_medview,name='approveorreject'),
    path('approve_staff/<int:staff_id>/', coordinator_views.admin_approve_staff, name='admin_approve_staff'),
    path('reject_staff/<int:staff_id>/', coordinator_views.admin_reject_staff, name='admin_reject_staff'),
    path('approve_med/<int:med_id>/', coordinator_views.admin_approve_medicine, name='admin_approve_medicine'),
    path('reject_med/<int:med_id>/', coordinator_views.admin_reject_medicine, name='admin_reject_medicine'),
    path('phome/',  pharmacist_views.pharmacy_homepage, name='phome'),
    path('medadd/',  pharmacist_views.add_medicine,name='medicine_add'),


    path('patient_data/',  coordinator_views.patient_data,name='patient_data'),
    path('patient_records/',  coordinator_views.patient_records,name='patient_records'),
    path('ptdel/<int:op_number>/', coordinator_views.patient_delete, name='ptdel'),
    path('ptconsultdel/<int:op_number>/<str:date>/', coordinator_views.patient_consult_delete, name='ptconsultdel'),




    path("adminmedview/", coordinator_views.admin_medicineview, name='admin_medicineview'),
    path("adminmeddel/<int:med_id>/", coordinator_views.admin_delete_medstock, name='admin_medicinedel'),
    path("adminmededit/<int:med_id>/", coordinator_views.admin_edit_medicine, name='admin_medicineedit'),
    path("adminmedupdate/<int:med_id>/", coordinator_views.admin_update_medstock, name='admin_medicineupdate'),



   path('rhome/', receptionist_views.receptionist_homepage, name='rhome'),

    path('patient_registration/', receptionist_views.patient_registration_submit, name='patient_registration_submit'),
    path('op_number/', receptionist_views.enter_op_number, name='enter_op_number'), 
    path('assign_doctor/<int:op_number>/', receptionist_views.assign_doctor, name='assign_doctor'),



    path('dhome/', doctor_views.doctor_homepage, name='dhome'),
    path('ptlist/', doctor_views.consultation_details, name='ptlist'),
    path('editpt/<int:op_number>/', doctor_views.edit_prescription_tbl, name='editpt'),


     path('consult/<int:op_number>/', doctor_views.consultation_page, name='consultation'),
    path('history/<int:op_number>/', doctor_views.consultation_history, name='history'),
    
    path('search_medicine/', doctor_views.search_result, name='search_result'),
    path('result_med/', doctor_views.search_result, name='result_med'),



    path("pharmacymedview/",pharmacist_views.pharmacisit_medicineview, name='pharmacymedview'),
    path('search_prescription/', pharmacist_views.search_prescription, name='search_prescription'),
    path('prescription_details/', pharmacist_views.prescription_details, name='prescription_details'),

    path('billing/',pharmacist_views.billing, name='billing'),
 
    path('get_medicine_details/', pharmacist_views.get_medicine_details, name='get_medicine_details'),
    path('save_bill/', pharmacist_views.save_bill, name='save_bill'),
    path('meddel/<int:mid>/',pharmacist_views. delete_bill),
    path('edit/<int:mid>/', pharmacist_views.edit_bill),
    path('medupdate/<int:mid>/',pharmacist_views. update_bill, name='update_bill'),
    path('seebill/',pharmacist_views.see_bill),
    path('proceed_bill/',pharmacist_views.proceed_bill, name='proceed_bill'),

    path('lgo/', pharmacist_views.logouts),







    

]

