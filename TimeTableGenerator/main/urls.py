from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate', views.generate, name='generate'),
    path('generate_timetable', views.generate, name='generate_timetable'),
]