from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.utils.timezone import now, make_aware
from django.contrib.auth import authenticate, login, logout
from myapp.models import enquiry_table,booking_table
from datetime import datetime
import pytz
# Create your views here.
def home(request):
    return render(request,'index.html')

def book(request):
    if request.method == 'POST':
        a=request.POST.get('name')
        b=request.POST.get('email')
        f=request.POST.get('phone')
        c=request.POST.get('date')
        d=request.POST.get('time')
        e=request.POST.get('people')
        m=request.POST.get('message')

        try:
            booking_datetime = datetime.strptime(f"{c} {d}", "%Y-%m-%d %H:%M")
            # Convert to aware datetime (based on project timezone)
            booking_datetime = make_aware(booking_datetime)
        except ValueError:
            messages.error(request, "Invalid date or time format.")
            return redirect('book')

        if booking_datetime < now():
            messages.error(request, "Please choose correct date!!!")
            return redirect('book')
        

        book=booking_table(name = a, email=b, phone=f, date=c, time=d, people=e, message=m)
        book.save()
        messages.success(request, 'Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!')
    return render(request, 'booking.html')

def contact(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('subject')
        d = request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, subject = c, message = d)
        enquiry.save()
        #messages.success(request, 'Enquiry Form Submitted Succesfully....')
        return redirect('/?submitted=true#contact')
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        a = request.POST['username']
        b = request.POST['password']
        
        user = authenticate(request, username = a, password = b)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')
    return render(request, 'login.html')

def dashboard(request):
    data=booking_table.objects.all()
    dict1={'information':data}
    return render(request,'dashboard.html',dict1)

def delete_record(request, id):
    if request.method == 'POST':
        data=booking_table.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/dashboard/')

def edit(request,id):
    info=booking_table.objects.filter(pk=id)
    data={'information':info}
    return render(request, 'edit.html', data)

def update_record(request,id):
    info=booking_table.objects.get(pk=id)
    info.name = request.POST.get('name')
    info.email = request.POST.get('email')
    info.phone = request.POST.get('phone')
    info.date = request.POST.get('date')
    info.time = request.POST.get('time')
    info.people = request.POST.get('people')
    info.message = request.POST.get('message')
    info.save()
    return HttpResponseRedirect('/dashboard/')