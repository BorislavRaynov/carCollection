from django.shortcuts import render, redirect
from .models import Car
from .forms import CreateCarForm, CarEditForm, DeleteCarForm
# Create your views here.
#create_car, car_details, car_edit, car_delete

def create_car(request):
    form = CreateCarForm()

    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'car_collection/car/car-create.html', context=context)

def car_details(request, car_id):
    car = Car.objects.filter(id=car_id).get()

    context = {
        'car': car
    }

    return render(request, 'car_collection/car/car-details.html', context=context)

def car_edit(request, car_id):
    car = Car.objects.filter(id=car_id).get()
    form = CarEditForm(instance=car)

    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car
    }

    return render(request, 'car_collection/car/car-edit.html', context=context)


def car_delete(request, car_id):
    car = Car.objects.filter(id=car_id).get()
    form = DeleteCarForm(instance=car)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car
    }

    return render(request, 'car_collection/car/car-delete.html', context=context)
