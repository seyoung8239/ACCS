import pprint

from django.shortcuts import render
from django.http import HttpResponse
from module.shelter import check_place
from module.heatwave_casualties_region import heatwave_casualties_region, heatwave_casualties_total
def index(request):
    res = check_place()
    return HttpResponse(res)

def heatwave_total(request):
    data = heatwave_casualties_total()

    return HttpResponse(data)


def heatwave_region(request):
    data = heatwave_casualties_region()

    return HttpResponse(data)