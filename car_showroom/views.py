from django.shortcuts import render
from django.http import HttpResponse
from .models import VehiclePart


def index(request):
    last_vehiclepart = VehiclePart.objects.order_by('-id')[0]
    return render(request, 'car_showroom/index.html', {
        'last_vehiclepart': last_vehiclepart,
    })

def vehiclepart(request, vehiclepart_id):
    return HttpResponse("You're looking at vehicle part # %s." % vehiclepart_id)

def section(request, section_id):
    response = "You're looking at the section # %s."
    return HttpResponse(response % section_id)

def top_priced(request):
    priciest_vehiclepart_list = VehiclePart.objects.order_by('-price')[:5]
    output = "<br>".join([f"{v.id}. Name: {v.name},  price: {v.price}"
        for v in priciest_vehiclepart_list])
    return HttpResponse(output)