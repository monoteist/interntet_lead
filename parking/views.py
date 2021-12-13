from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ParkingSpace


class ParkingListView(ListView):
    queryset = ParkingSpace.objects.all()[:2]
    context_object_name = 'parking_spaces'
    template_name = 'parking.html'


class ParkingReserveView(UpdateView):
    model = ParkingSpace
    fields = '__all__'
    template_name = 'reserve_parking_space.html'


class ParkingDeleteView(DeleteView):
    model = ParkingSpace
    context_object_name = 'space'
    success_url = reverse_lazy('parking')
    template_name = 'parking_space_delete.html'
