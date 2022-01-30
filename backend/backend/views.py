import pprint

from django.shortcuts import render
from django.http import HttpResponse
from module.shelter import check_place
def index(request):
    res = check_place()
    return HttpResponse(res)