from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("sala/<int:id>", views.detalle_sala, name="detalle_sala"),
    path("reservar/", views.crear_reserva, name="crear_reserva"),
]