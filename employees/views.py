from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth
from .models import seminars
from .models import workshops
from turtle import pos


def home(request):
    return render(request, 'employees/home.html')


def TrainingView(request):
    if request.method == 'POST':
        title1= request.POST['title1']
        bdate = request.POST['bdate']
        address = request.POST['address']
        type = request.POST['type']
        conducted = request.POST['conducted']
        level = request.POST['level']

        saveSeminars = seminars(title1=title1, bdate=bdate, address=address, type=type, conducted=conducted, level=level)
        saveSeminars.save()
    return render(request, 'employees/addSeminar.html')

def viewTraining(request):
    viewTrains = seminars.objects.all()
    return render(request, 'employees/viewSeminar.html', {'viewTrains': viewTrains})


def WorkshopView(request):
    if request.method == 'POST':
        title1= request.POST['title1']
        bdate = request.POST['bdate']
        address = request.POST['address']
        type = request.POST['type']
        conducted = request.POST['conducted']
        level = request.POST['level']
        saveWorkshops = workshops(title1=title1, bdate=bdate, type=type, address=address, conducted=conducted, level=level)
        saveWorkshops.save()
    return render(request, 'employees/addWorkshop.html')

def viewWorkshop(request):
    viewWorkshop = workshops.objects.all()
    return render(request, 'employees/viewWorkshop.html', {'viewWorkshop': viewWorkshop})

def edit_wokshop(request):
    viewWorkshop =workshops.objects.get(id=pid)
    if request.method == "POST":
        title1 = request.POST['title1']
        bdate = request.POST['bdate']
        address = request.POST['address']
        type = request.POST['type']
        conducted = request.POST['conducted']
        level = request.POST['level']
        saveWorkshops = workshops(title1=title1, bdate=bdate, type=type, address=address, conducted=conducted,
                                  level=level)
        messages.success(request, "workshops Updated successfully")
        return redirect('viewWorkshop')
    return render(request, 'employees/viewWorkshop.html', {'viewWorkshop': viewWorkshop})





def createEmployeee(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        post = request.POST['post']
        emp_obj = Employee.objects.create(name=name,dob=dob,doj=doj,address=address,city=city,state=state,zipcode=zipcode,country=country,department=department,post=post)
        messages.success(request, "Employee created successfully")
        return redirect('employee_list')
    return render(request, 'employees/create_employeee.html')

def employee_list(request):
    emp_data = Employee.objects.filter()
    d = {'employee':emp_data}
    return render(request, 'employees/employee_list.html',d)

def edit_employee(request, pid):
    emp_data =Employee.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        post = request.POST['post']
        emp_obj = Employee.objects.filter(id=pid).update(name=name,dob=dob,doj=doj,address=address,city=city,state=state,zipcode=zipcode,country=country,department=department,post=post)
        messages.success(request, "Employee Updated successfully")
        return redirect('employee_list')
    return render(request, 'employees/edit_employeee.html', {'emp_data':emp_data})

def delete_employee(request, pid):
    data = Employee.objects.get(id=pid)
    data.delete()
    messages.success(request, "Employee Deleted successfully")
    return redirect('employee_list')
