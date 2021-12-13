from django.views.generic import ListView, UpdateView

from .models import ParkingSpace


class ParkingListView(ListView):
    queryset = ParkingSpace.objects.all()[:2]
    context_object_name = 'parking_spaces'
    template_name = 'parking.html'

class ParkingReserveView(UpdateView):
    model = ParkingSpace
    fields = '__all__'
    template_name = 'reserve_parking_space.html'