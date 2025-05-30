from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ReservationForm
from django.urls import reverse_lazy


from .serializer import *
from .models import *

# Create your views here.
def reservas_view(request):
    return render(request, 'index.html')

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class RoomAmenityViewSet(viewsets.ModelViewSet):
    queryset = RoomAmenity.objects.all()
    serializer_class = RoomAmenitySerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ReservationListView(ListView):
    model = VistaReservasCompletas
    template_name = 'reservations/index.html'
    context_object_name = 'reservas'

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/form.html'
    success_url = reverse_lazy('reservation_list')

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/form.html'
    success_url = reverse_lazy('reservation_list')

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservations/confirm_delete.html'
    success_url = reverse_lazy('reservation_list')