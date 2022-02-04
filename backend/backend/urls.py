from django.contrib import admin
from django.urls import path
from .views import heatwave_total, heatwave_region
from websocket import views
from .views import heatwave_total, heatwave_region, inquiry_response_heatwave_by_field, find_shelter, \
    get_each_region_temperature_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shelter/', find_shelter),
    path('heatwave/total', heatwave_total),
    path('heatwave/region', heatwave_region),
    path('heatwave/response/<str:field>', inquiry_response_heatwave_by_field),
    path('temperatureInfo/', get_each_region_temperature_info),
    path('ShareMe/', views.ShareMe.as_view()),
    path('Alarm/', views.Alarm.as_view()),
]

"""
    heatwave/response/<str:field> field 의 형태
    'public', 'vulnerable', 'industry', 'livestock', 'agriculture', 'aquaculture', 'etc'
"""
