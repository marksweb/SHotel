import random
import decimal

from apps.management.models import RoomType


def create_rooms():
    ROOM_TYPES = ('Single', 'Double', 'King', 'Twin',
                  'Suite', 'President Suite', 'Apartment',)

    for room_type in ROOM_TYPES:
        type_of_room = RoomType.objects.create(name=room_type)
        for _ in range(2):
            type_of_room.rooms.create(
                number=random.randint(100, 199),
                price=float(decimal.Decimal(
                    random.randrange(1000, 10000)) / 100),
                is_for_disabled=random.choice([True, False]),
                is_for_smokers=random.choice([True, False])
            )
