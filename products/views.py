from django.http import HttpResponse
from django.shortcuts import redirect, render
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
