from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.forms.forms import CarForm
from products.models import Car
def home(request):
    return render(request, 'home.html')

def delete(request,id):
    car = Car.objects.get(id=id)
    if car is None:
        return HttpResponse("Car not found")
    
    car.delete()
    return redirect("/inventory")


def inventory(request):
    cars= Car.objects.all()
    return render(request, 'inventory.html', {"cars":cars})


def details(request,id):
    cars = get_object_or_404(Car, id=id)
    
    return render(request, "details.html", { "car": cars })


def create(request):
    
    if request.method == "GET":
        form = CarForm()
        
        return render(request,"create.html",{"form":form})
    
    form = CarForm(request.POST)
    if form.is_valid():
       
        form.save()
        return redirect("/")
    
    
    return redirect(request,"/create",{"form":form})


def edit(request,id):
    product = get_object_or_404(Car, id=id)
    
    if request.method == "GET":
        form = CarForm(instance=product)
        return render(request,"edit.html",{"form":form})
    
    form = CarForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/")
    
    return render(request,"edit.html",{"form":form})

