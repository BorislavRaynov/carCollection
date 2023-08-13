from django.shortcuts import render, redirect
from car_collection.car.models import Car
from .models import Profile
from .forms import CreateProfileForm, EditProfileForm
# Create your views here.

def create_profile(request):
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'car_collection/auth_app/profile-create.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'car_collection/auth_app/profile-edit.html', context=context)

def details_profile(request):

    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_sum = sum([car.price for car in cars])

    current_name = ""

    if profile.first_name:

        current_name += f"{profile.first_name} "

    if profile.last_name:
        current_name += f"{profile.last_name}"

    context = {
        'profile': profile,
        'cars': cars,
        'current_name': current_name,
        'total_sum': total_sum
    }

    return render(request, 'car_collection/auth_app/profile-details.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    if request.method == 'POST':
        cars.delete()
        profile.delete()
        return redirect('home-page')

    return render(request, 'car_collection/auth_app/profile-delete.html')
