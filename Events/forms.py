from django import forms
from .models import Event
from django.core.exceptions import ValidationError

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['organizer', 'name', 'description', 'location', 'maxcapacity', 'ticketprice', 'category', 'status', 'startdate', 'enddate']

  # Validación personalizada para el campo 'name'
  def clean_name(self):
    name = self.cleaned_data.get('name')
    if 'canceled' in name.lower():
      raise ValidationError('The event name cannot contain the word "Canceled".')
    return name
    

