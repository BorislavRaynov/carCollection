from django.urls import path
from .views import create_car, car_details, car_edit, car_delete

urlpatterns = [
    path('create/', create_car, name='create-car'),
    path('details/<int:car_id>', car_details, name='car-details'),
    path('edit/<int:car_id>', car_edit, name='car-edit'),
    path('delete/<int:car_id>', car_delete, name='car-delete'),
]
