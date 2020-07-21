from ...models import Room, RoomType


class TestRoom:

    def setUp(self):
        self.room_type = RoomType.objects.create(name='Premium')
        self.room = Room.objects.create(number=110,
                                        room_type=self.room_type,
                                        price=123.34,
                                        is_for_disabled=False,
                                        is_for_smokers=False,
                                        comment=None)

    def test_is_room(self):
        assert isinstance(self.room, Room)
        assert isinstance(self.room_type, RoomType)
