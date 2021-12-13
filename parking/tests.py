from datetime import date

from django.test import TestCase

from .models import ParkingSpace

class ParkingTests(TestCase):
    def test_create_parking_space(self):
        parking_space = ParkingSpace.objects.create(
            status = 'reserved',
            time = date(2021, 12, 14)
        )
        self.assertEqual(parking_space.status, 'reserved')
        self.assertEqual(parking_space.time, date(2021, 12, 14))