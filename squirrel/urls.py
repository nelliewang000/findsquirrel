
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('map/', views.map),
    path('sightings/',views.list),
    path('sightings/add/', views.add),
    path('sightings/stats/', views.stats, name='stats'), 
    path('sightings/<str:sq_id>/',views.detail),  
    ]
