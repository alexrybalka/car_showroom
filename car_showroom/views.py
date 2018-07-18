from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import VehiclePart, Section


def index(request):
    return render(request, 'car_showroom/index.html', {
        'amount_vehiclepart': VehiclePart.objects.all().count(),
    })

def sections(request):
    return render(request, 'car_showroom/sections.html', {
        'section_list': Section.objects.all(),
    })

def section(request, section_name):
    vehiclepart_list = VehiclePart.objects.order_by('-name')
    template = loader.get_template('car_showroom/<section_name>/')
    context = {
        'vehiclepart_list': vehiclepart_list,
    }
    return HttpResponse(template.render(context, request))

def top_priced(request):
    priciest_vehiclepart_list = VehiclePart.objects.order_by('-price')[:5]
    return render(request, 'car_showroom/top-priced.html', {
        'priciest_vehiclepart_list': priciest_vehiclepart_list,
    })
