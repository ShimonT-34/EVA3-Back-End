from django import forms
from .models import Reserva
from django.utils import timezone
from datetime import timedelta

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut', 'sala'] #SON LOS CAMPOS DE RESERVA