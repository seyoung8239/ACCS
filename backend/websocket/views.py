from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
import json
from django.shortcuts import HttpResponse


# Create your views here.


class Alarm(TemplateView):
    template_name = "templates/alarm.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        context['username'] = self.request.user.username
        return context


class ShareMe(TemplateView):
    template_name = "templates/ShareMe.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        context['username'] = self.request.user.username
        return context

    def post(self, request, **kwargs):
        ins = models.Alarm()
        print('2')
        data_unicode = request.body.decode('utf-8')
        data = json.loads(data_unicode)
        ins.message = data['message']
        ins.la = data['la']
        ins.lo = data['lo']
        ins.save()
        return HttpResponse('')
