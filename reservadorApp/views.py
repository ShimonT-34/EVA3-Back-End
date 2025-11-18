from django.shortcuts import render

# Create your views here.

def saludar(request): 
    return render(request, 'home.html') 