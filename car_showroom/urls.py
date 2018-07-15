from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vehiclepart_id>/vehiclepart/', views.vehiclepart, name='vehiclepart'),
    path('<int:section_id>/section/', views.section, name='section'),
]