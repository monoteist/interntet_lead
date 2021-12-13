from django.urls import path
from .views import ParkingView

urlpatterns = [
    path('', ParkingView.as_view(), name='parking')
]
