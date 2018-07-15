from django.shortcuts import render
from django.http import HttpResponse


def vehiclepart(request, vehiclepart_id):
    return HttpResponse("You're looking at vehicle part # %s." % vehiclepart_id)

def section(request, section_id):
    response = "You're looking at the section # %s."
    return HttpResponse(response % section_id)

def index(request):
    return HttpResponse("Hello, world. You're at the best car showroom ever. Congrats!")