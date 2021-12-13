from django.views.generic import ListView

from .models import ParkingSpace


class ParkingView(ListView):
    queryset = ParkingSpace.objects.all()[:2]
    context_object_name = 'parking_spaces'
    template_name = 'parking.html'