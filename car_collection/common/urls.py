from django.urls import path
from .views import index, catalogue

urlpatterns = [
    path('', index, name='home-page'),
    path('catalogue/', catalogue, name='catalogue')
]