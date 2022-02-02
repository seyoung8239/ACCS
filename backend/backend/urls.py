from django.contrib import admin
from django.urls import path
from . import views
from .views import heatwave_total, heatwave_region, inquiry_response_heatwave_by_field

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('heatwave/total', heatwave_total),
    path('heatwave/region', heatwave_region),
    path('heatwave/response/<str:field>', inquiry_response_heatwave_by_field),
]

"""
    heatwave/response/<str:field> field 의 형태
    'public', 'vulnerable', 'industry', 'livestock', 'agriculture', 'aquaculture', 'etc'
"""
