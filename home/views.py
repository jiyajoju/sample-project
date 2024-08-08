from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor
from .forms import bookingform
def index(request):
     return render(request,"index.html")
    #return HttpResponse("hello world")
# Create your views here.
def about(request):
      #return render(request,"hello.html",{'range':range(1,11)})
    return HttpResponse("about us")
#def show(request):
     # number1={
          #  'num':[1,2,3,4,5,6,7,8,9,10]
     # }
     # return render(request,"show.html",number1)

def dept(request):
      dic_dept={
           'depts':Department.objects.all()
      }
      return render(request,"dept.html",dic_dept)
def doctors(request):
      dic_doctor={
           'doctor1':Doctor.objects.all()
      }
      return render(request,"doctor.html",dic_doctor)

def book(request):
     if request.method=="POST":
          form=bookingform(request.POST)
          if form.is_valid():
               form.save()
     else:
          form=bookingform()
     dic_form={
          'form':form
     }
     return render(request,"booking.html",dic_form)