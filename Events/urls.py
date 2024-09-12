from django.urls import path
from .views import EventCreateView, EventUpdateView
from .views import OrganizerListView, OrganizerCreateView

urlpatterns = [
  path('create/', EventCreateView.as_view(), name='event_create'),
  path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
  path('organizers/', OrganizerListView.as_view(), name='organizer_list'),
  path('organizers/create/', OrganizerCreateView.as_view(), name='organizer_create'),
]