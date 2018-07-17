from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('top-priced/', views.top_priced, name='top-priced'),
    path('vehicle-part/<int:vehiclepart_id>', views.vehiclepart, name='vehicle-part'),
    path('section/<int:section_id>/', views.section, name='section'),
]