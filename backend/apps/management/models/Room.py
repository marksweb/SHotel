from django.db import models


class Room(models.Model):
    number = models.IntegerField()
    room_type = models.ForeignKey('management.RoomType', on_delete=models.CASCADE,
                                  related_name='rooms')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_available = models.BooleanField(default=True)
    is_for_disabled = models.BooleanField()
    is_for_smokers = models.BooleanField()
    comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.number)
