from django.urls import path
from .views import ParkingListView, ParkingReserveView

urlpatterns = [
    path('', ParkingListView.as_view(), name='parking'),
    path('<int:pk>', ParkingReserveView.as_view(), name='parking_reserve')

]
