from django.shortcuts import render, redirect, get_object_or_404
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

    #para liberar salas
    if reserva and reserva.fecha_termino < timezone.now():
        sala.disponible = True
        sala.save()

    return render(request, 'detalle_sala.html', {
        "sala": sala,
        "reserva": reserva,
    })

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

    return render(request, "crear_reserva.html", {'form': form})