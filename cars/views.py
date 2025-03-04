from django.shortcuts import render
from cars.models import Car

def car_view(request):
    #cars = Car.objects.all()
    cars = Car.objects.filter(brand__name='Fiat')

    return render(request=request, template_name='cars.html', context={'cars': cars})
