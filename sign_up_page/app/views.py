from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import *

# Create your views here.
def registration(request):
    return render(request,"registration.html")

def create_user(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        city = request.POST['city']
        date = request.POST['date']
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email Already Exists")
        else:
            User.objects.create(fname=fname, lname=lname, email=email, password=password ,city=city, date=date)
            return redirect('/table/')
        
def table(request):
    data=User.objects.all()
    return render(request, "table.html", {"data":data})

def delete_user(request,pk):
    User.objects.get(id=pk).delete()
    return redirect('/table/')

def update_user(request,uid):
    user_obj = User.objects.get(id=uid)
    return render(request, "update.html", {"user_obj":user_obj})

def update_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST['email']
        date = request.POST['date']
        city = request.POST['city']
        User.objects.filter(id=uid).update(fname=fname, lname=lname, email=email, date=date, city=city)
        return HttpResponse("User Update Sucessfully")

