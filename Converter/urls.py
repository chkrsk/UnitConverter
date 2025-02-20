from django.urls import path
from . import views

urlpatterns = [
    path('', views.length_calc, name=''),
    path('weight-calc', views.weight_calc, name='weight-calc'),
    path('temperature-calc', views.temperatur_calc, name='temperature-calc'),
]
