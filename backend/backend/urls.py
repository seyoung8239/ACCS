from django.contrib import admin
from django.urls import path
from . import views
from .views import heatwave_total, heatwave_region

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('heatwave/total', heatwave_total),
    path('heatwave/region', heatwave_region)
]
