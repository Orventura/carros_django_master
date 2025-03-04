from django.shortcuts import render
from cars.models import Car

def car_view(request):
    cars = Car.objects.all().order_by('brand__name', 'model')
    print(request.GET.get('search'))

    search = request.GET.get('search')

    #cars = Car.objects.filter(brand__name='Chevrolet')
    if search:    
        cars = Car.objects.filter(model__icontains=search).order_by('brand__name', 'model')


    return render(request=request, template_name='cars.html', context={'cars': cars})
