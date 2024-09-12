from django.db import models
from django.core.exceptions import ValidationError

#Organizer model
class Organizer(models.Model):
  name = models.CharField(max_length=256)
  email = models.EmailField(max_length=256)
  phone = models.CharField(max_length=256)
  address = models.CharField(max_length=256, blank=True, null=True)
  website = models.URLField(max_length=256, blank=True, null=True)
  registrationdate = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name


#Event model
class Event(models.Model):
  CATEGORY_CHOICES = [
    ('concert', 'Concert'),
    ('conference', 'Conference'),
    ('sport', 'Sport'),
    ('social', 'Social'),
  ]

  STATUS_CHOICES = [
    ('active', 'Active'),
    ('preparation', 'Preparation'),
    ('canceled', 'Canceled'),
  ]

  organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='events')
  name = models.CharField(max_length=256)
  description = models.TextField()
  location = models.CharField(max_length=256)
  maxcapacity = models.IntegerField()
  ticketprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
  status = models.CharField(max_length=64, choices=STATUS_CHOICES, default='active')
  startdate = models.DateTimeField()
  enddate = models.DateTimeField()

  def clean(self):
    if 'canceled' in self.name.lower():
      raise ValidationError('The event name cannot contain the word "Canceled".')

  def __str__(self):
    return self.name


