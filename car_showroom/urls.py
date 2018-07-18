from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('top-priced/', views.top_priced, name='top-priced'),
    path('car_showroom/<section_name>/', views.section, name='section'),
    path('sections/', views.sections, name='sections'),
]