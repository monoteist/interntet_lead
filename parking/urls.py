from django.urls import path
from .views import ParkingListView, ParkingReserveView, ParkingDeleteView

urlpatterns = [
    path('', ParkingListView.as_view(), name='parking'),
    path('reserve/<int:pk>/', ParkingReserveView.as_view(), name='parking_reserve'),
    path('delete/<int:pk>/', ParkingDeleteView.as_view(), name='parking_delete')
]
