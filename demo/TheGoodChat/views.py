from django.shortcuts import render
from django.http import HttpResponse
from .models import car
from .forms import carForms
# Create your views here.
listofusers=[{"Name":"Aly","Age":"22","salary":"12000"}
            ,{"Name":"Shimaa","Age":"23","salary":"20000"}
            ,{"Name":"Abdo","Age":"23","salary":"12000"}]
dict={"Data":listofusers}
def renderhtml(request):
    return render(request, 'TheGoodChat/index.html',dict)

app_name='TheGoodChat'

def viewcars(request):
    result=car.objects.all()
    dict2={"cars":result}
    return render(request,'TheGoodChat/cars.html',dict2)

def CreateCar(request):
    car=carForms(request.POST,request.FILES)
    if car.is_valid():
        car.save()
    return render(request,'TheGoodChat/createcar.html',{"Form":carForms})


def ShowCarWithID(request,ID):
    carid= car.objects.get(id = ID)
    return render(request,'TheGoodChat/cardetails.html',{"onecar":carid})

def DeleteCarWithID(request,ID):
    carid= car.objects.get(id = ID)
    carid.delete()
    result=car.objects.all()
    dict2={"cars":result}
    return render(request,'TheGoodChat/cars.html',dict2)

def UpdateCarWithID(request,ID):
    carid= car.objects.get(id = ID)
    form=carForms(request.POST or None, instance=carid)
    if form.is_valid():
        form.save()
        result=car.objects.all()
        dict2={"cars":result}
        return render(request,'TheGoodChat/cars.html',dict2)
    return render(request,'TheGoodChat/updatecar.html',{"onecar":carid,"form":form})