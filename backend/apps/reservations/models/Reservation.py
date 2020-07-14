from datetime import date

from django.db import models
from django.core.exceptions import ValidationError


class Reservation(models.Model):
    room = models.ForeignKey('management.Room', related_name='reservations',
                             on_delete=models.CASCADE)
    guest = models.ForeignKey('reservations.Guest', related_name='reservations',
                              on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    made_by = models.ForeignKey('management.Employee', related_name='reservations',
                                on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = (('room', 'guest', 'check_in'),
                           ('room', 'guest', 'check_out'),)
        ordering = ('check_out',)

    def clean(self):
        super().clean()

        if self.check_in < date.today() or self.check_out < date.today():
            raise ValidationError('Date cannot be in the past.')
        if self.check_in >= self.check_out:
            raise ValidationError('Reservation must last at least one day.')
        if not self.room.is_available:
            raise ValidationError('Room is occupied.')
    
    def save(self):
        super().save()

        self.room.is_available = False
        self.room.save()

    def __str__(self):
        return f'Reservation for {self.guest.first_name} \
            {self.guest.last_name} - Room {self.room.number}'
