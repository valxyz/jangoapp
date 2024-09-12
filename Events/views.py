from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import Event, Organizer
from .forms import EventForm
from django.contrib.auth.mixins import LoginRequiredMixin

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')


class OrganizerListView(ListView):
    model = Organizer
    template_name = 'organizer_list.html'  
    context_object_name = 'organizers'

class OrganizerCreateView(CreateView):
    model = Organizer
    template_name = 'organizer_form.html'  # La plantilla que vamos a utilizar para el formulario
    fields = ['name', 'email', 'phone', 'address', 'website', 'active']  # Campos del modelo que queremos en el formulario
    success_url = reverse_lazy('organizer_list')  # Redirige a la lista de organizadores después de crear uno nuevo


def home(request):
    return render(request, 'home.html') 

def login(request):
    return render(request, 'login.html')

def events(request):
    events = Event.objects.all()  # Obtener todos los eventos
    return render(request, 'events.html', {'events': events} ) 


