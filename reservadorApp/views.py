from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Sala, Reserva
from .forms import ReservaForm

# Create your views here.

def home(request):
    context = {
        'salas' : Sala.objects.all(),
        }

    return render(request, 'home.html', context)

def detalle_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    reserva = Reserva.objects.filter(sala=sala).order_by('-id').first()
    context = {
        "sala" : sala,
        "reserva" : reserva,
    }

    #para liberar salas
    if reserva and reserva.fecha_termino < timezone.now():
        sala.disponible = True
        sala.save()

    return render(request, 'detalle_sala.html', context)

class SalaListView(generic.ListView):
    model = Sala
    template_name = "lista_salas.html"
    context_object_name = "salas"

    #Trae la lista, y la ordena por nombre
    def get_queryset(self):
        return Sala.objects.all().order_by('nombre')

def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            # al reservar cambia a no disponible
            reserva.sala.disponible = False
            reserva.sala.save()
            return redirect('home')
    else:
        form = ReservaForm()

    context = {
        "form":form,
        }

    return render(request, "crear_reserva.html", context)