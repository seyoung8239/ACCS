from api_module.shelter import check_place
from django.http import HttpResponse
from api_module import heatwave_casualties_region, shelter
from django.http import HttpResponse
from api_module import shelter, heatwave_casualties_region


def index(request):
    res = shelter.check_place()
    return HttpResponse(res)


def heatwave_total(request):
    data = heatwave_casualties_region.heatwave_casualties_total()

    return HttpResponse(data)


def heatwave_region(request):
    data = heatwave_casualties_region.heatwave_casualties_region()

    return HttpResponse(data)
