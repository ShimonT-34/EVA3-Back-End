from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("sala/<int:id>", views.detalle_sala, name="detalle_sala"),
    path("lista_salas/", views.SalaListView.as_view(), name="lista_salas"),
    path("reservar/", views.crear_reserva, name="crear_reserva"),
]