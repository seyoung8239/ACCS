from django.http import HttpResponse
from api_module import shelter, heatwave_casualties_region, inquiry_response_heatwave, get_regions_temperature_info


def find_shelter(request):
    res = shelter.check_place()
    return HttpResponse(res)


def heatwave_total(request):
    data = heatwave_casualties_region.heatwave_casualties_total()

    return HttpResponse(data)


def heatwave_region(request):
    data = heatwave_casualties_region.heatwave_casualties_region()

    return HttpResponse(data)


def inquiry_response_heatwave_by_field(request, field):
    """ 분야(field)별 폭염 대응 기준 조회 """

    data = inquiry_response_heatwave.get_action_by_field(field)

    return HttpResponse(data)


def get_each_region_temperature_info(request):
    data = get_regions_temperature_info.weather_info_parsing()

    return HttpResponse(data)
