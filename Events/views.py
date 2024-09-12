from django.shortcuts import render
from .models import Event


def home(request):
    return render(request, 'home.html') 

def login(request):
    return render(request, 'login.html')

def events(request):
    events = Event.objects.all()  # Obtener todos los eventos
    return render(request, 'events.html', {'events': events} ) 
