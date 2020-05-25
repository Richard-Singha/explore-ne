from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Destination, Festival, Hotspot, Stay, PopularFood, Image

def indexView(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})

def get_festivals(request, Destination_id):
    my_festival = Festival.objects.filter(destination_id=Destination_id)
    my_place = Hotspot.objects.filter(destination_id=Destination_id)
    my_food = PopularFood.objects.filter(destination_id=Destination_id)
    my_stay = Stay.objects.filter(destination_id=Destination_id)
    return render(request, 'destinations.html', {'repr': my_festival, 'places': my_place, 'foods': my_food, 'stays': my_stay})

# def get_places(request, Destination_id):
#     my_place = Hotspot.objects.filter(destination_id=Destination_id)
#     return render(request, 'destinations.html', {'places': my_place})
