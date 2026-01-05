from django.shortcuts import render,redirect
from django.utils import timezone
from django.db import models


from app1.models import Hostel,Room,Student,Complaint,Visitor,Payment
from app1.form import hostel_form,room_form,student_form,complaint_form,visitor_form,payment_form
from app1.form1 import hostel_update_form,room_update_form,student_update_form,complaint_update_form,visitor_update_form,payment_update_form

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

DEFAULT_DELETE_USERNAME = "venky"
DEFAULT_DELETE_PASSWORD = "venky@7619"



def registration_form(request):
    message=''
    if request.method=='POST':
        username=request.POST.get('username')
        user_email=request.POST.get('useremail')
        p1=request.POST.get('user_password')
        p2=request.POST.get('user_con_password')

        if p1!=p2:
            message='enter correct password'

        elif User.objects.filter(email=user_email).exists():
            message='user Exit'

        else:
            user=User.objects.create_user(username=username,email=user_email,password=p1)
            user.save()
            message='user created'
            return redirect('login101')

    return render(request,'regi/register.html',{'message':message})

def login_form(request):
    message=''

    if request.method=='POST':

        username=request.POST.get('user_log_name')
        password=request.POST.get('user_log_password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            message='login sucessfully'
            return redirect('dashboard')

        else:
            message='invalid detaills'

    return  render(request,'regi/rampo.html',{'message':message})






def dashboard(request):
    hostel_count = Hostel.objects.count()
    room_count = Room.objects.count()

    student_count = Student.objects.count()
    complaint_count = Complaint.objects.filter(status='Open').count()
    visitor_count = Visitor.objects.filter(approved=True).count()


    payment_total = Payment.objects.filter(
        paid=True
    ).aggregate(total=models.Sum('amount'))['total'] or 0

    context = {
        'hostel_count': hostel_count,
        'room_count': room_count,
        'student_count': student_count,
        'complaint_count': complaint_count,
        'visitor_count': visitor_count,
        'payment_total': payment_total,
    }

    return render(request,'dash.html', context)



def hostel_details(request):
    data=Hostel.objects.all()
    context={
        'data':data
    }
    return render(request,'hostel/hostel.html',context)
def hst_form(request):
    if request.method=='POST':
        form=hostel_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostel')
    else:
        form=hostel_form()
    context={
        'form':form
    }
    return render(request,'hostel/hostel_form.html',context)
def hst_update(request,id):
    data=Hostel.objects.get(id=id)
    if request.method=='POST':
        form=hostel_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('hostel')
    else:
        form=hostel_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'hostel/hostel_form.html',context)
def hst_delete(request, id):
    data = Hostel.objects.get(id=id)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == DEFAULT_DELETE_USERNAME and password == DEFAULT_DELETE_PASSWORD:
            data.delete()
            return redirect('hostel')

    return render(request, 'delete_auth.html')


def room_details(request):
    data=Room.objects.all()
    context={
        'data':data
    }
    return render(request,'room/room.html',context)
def rom_form(request):
    if request.method=='POST':
        form=room_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room')
    else:
        form=room_form()
    context={
        'form':form
    }
    return render(request,'room/room_form.html',context)
def room_update(request,id):
    data=Room.objects.get(id=id)
    if request.method=='POST':
        form=room_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('room')
    else:
        form=room_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'room/room_form.html',context)
def room_delete(request, id):
    data = Room.objects.get(id=id)

    if request.method == "POST":
        if (
            request.POST.get("username") == DEFAULT_DELETE_USERNAME and
            request.POST.get("password") == DEFAULT_DELETE_PASSWORD
        ):
            data.delete()
            return redirect('room')

    return render(request, 'delete_auth.html')


def std_details(request):
    data=Student.objects.all()
    context={
        'data':data
    }
    return render(request,'student/student.html',context)
def std_form(request):
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std')
    else:
        form=student_form()
    context={
        'form':form
    }
    return render(request,'student/student_form.html',context)
def std_update(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        form=student_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('std')
    else:
        form=student_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'student/student_form.html',context)
def std_delete(request, id):
    data = Student.objects.get(id=id)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if (
            username == DEFAULT_DELETE_USERNAME and
            password == DEFAULT_DELETE_PASSWORD
        ):
            data.delete()
            return redirect('std')
        else:
            return render(
                request,
                'delete_auth.html',
                {'error': 'Invalid credentials'}
            )

    return render(request, 'delete_auth.html')


def compl_details(request):
    data=Complaint.objects.all()
    context={
        'data':data
    }
    return render(request,'complaint/complaint.html',context)
def compl_form(request):
    if request.method=='POST':
        form=complaint_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint')
    else:
        form=complaint_form()
    context={
        'form':form
    }
    return render(request,'complaint/complaint_form.html',context)
def compl_update(request,id):
    data=Complaint.objects.get(id=id)
    if request.method=='POST':
        form=complaint_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('complaint')
    else:
        form=complaint_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'complaint/complaint_form.html',context)
def compl_delete(request, id):
    data = Complaint.objects.get(id=id)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == DEFAULT_DELETE_USERNAME and password == DEFAULT_DELETE_PASSWORD:
            data.delete()
            return redirect('complaint')
        else:
            return render(request, 'delete_auth.html', {'error': 'Invalid credentials'})

    return render(request, 'delete_auth.html')


def visit_details(request):
    data=Visitor.objects.all()
    context={
        'data':data
    }
    return render(request,'visitor/visitor.html',context)
def visit_form(request):
    if request.method=='POST':
        form=visitor_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor')
    else:
        form=visitor_form()
    context={
        'form':form
    }
    return render(request,'visitor/visitor_form.html',context)
def visit_update(request,id):
    data=Visitor.objects.get(id=id)
    if request.method=='POST':
        form=visitor_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('visitor')
    else:
        form=visitor_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'visitor/visitor_form.html',context)
def visit_delete(request, id):
    data = Visitor.objects.get(id=id)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == DEFAULT_DELETE_USERNAME and password == DEFAULT_DELETE_PASSWORD:
            data.delete()
            return redirect('visitor')
        else:
            return render(request, 'delete_auth.html', {'error': 'Invalid credentials'})

    return render(request, 'delete_auth.html')


def pay_details(request):
    data=Payment.objects.all()
    context={
        'data':data
    }
    return render(request,'payment/payment.html',context)
def pay_form(request):
    if request.method=='POST':
        form=payment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pay')
    else:
        form=payment_form()
    context={
        'form':form
    }
    return render(request,'payment/payment_form.html',context)
def pay_update(request,id):
    data=Payment.objects.get(id=id)
    if request.method=='POST':
        form=payment_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('pay')
    else:
        form=payment_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'payment/payment_form.html',context)
def pay_delete(request, id):
    data = Payment.objects.get(id=id)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == DEFAULT_DELETE_USERNAME and password == DEFAULT_DELETE_PASSWORD:
            data.delete()
            return redirect('pay')
        else:
            return render(request, 'delete_auth.html', {'error': 'Invalid credentials'})

    return render(request, 'delete_auth.html')
