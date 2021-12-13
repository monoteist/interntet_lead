from django.db import models


class ParkingSpace(models.Model):
    STATUS_CHOICES = (('reserved', 'зарезервировано'),
                      ('not_reserved', 'не зарезервировано'))
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='not_reserved')
    time = models.DateTimeField()

    def __str__(self) -> str:
        return f'Парковочное место № {self.pk} {self.status}'