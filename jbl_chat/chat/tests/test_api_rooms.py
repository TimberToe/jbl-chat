from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from chat.models import ChatRoom, ChatRoomMember, ChatRoomMessage


class RoomListApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.malin = User.objects.create(username="Malin")
        cls.fredrika = User.objects.create(username="Fredrika")
        cls.kalle = User.objects.create(username="kalle")
        cls.client = APIClient()
        cls.room_url = reverse("room-list")

    def test_user_not_part_of_any_rooms_gives_no_rooms(self):
        room = ChatRoom.objects.create(name="room1")
        ChatRoomMember.objects.create(member=self.fredrika, chatRoom=room)
        ChatRoomMember.objects.create(member=self.kalle, chatRoom=room)

        self.client.force_authenticate(user=self.malin)
        response = self.client.get(self.room_url)

        self.assertNotContains(response, text=room.name, status_code=status.HTTP_200_OK)

    def test_user_in_room_gives_only_that_room(self):
        room1 = ChatRoom.objects.create(name="room1")
        ChatRoomMember.objects.create(member=self.fredrika, chatRoom=room1)
        ChatRoomMember.objects.create(member=self.kalle, chatRoom=room1)

        room2 = ChatRoom.objects.create(name="room2")
        ChatRoomMember.objects.create(member=self.fredrika, chatRoom=room2)
        ChatRoomMember.objects.create(member=self.malin, chatRoom=room2)

        self.client.force_authenticate(user=self.malin)
        response = self.client.get(self.room_url)

        self.assertNotContains(
            response, text=room1.name, status_code=status.HTTP_200_OK
        )
        self.assertContains(response, text=room2.name, status_code=status.HTTP_200_OK)

    def test_no_rooms_give_empty_response(self):

        self.client.force_authenticate(user=self.malin)
        response = self.client.get(self.room_url)

        self.assertListEqual(response.data, [])


class RoomDetailApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.malin = User.objects.create(username="Malin")
        cls.fredrika = User.objects.create(username="Fredrika")
        cls.kalle = User.objects.create(username="kalle")

        cls.room1 = ChatRoom.objects.create(name="room1")
        ChatRoomMember.objects.create(member=cls.fredrika, chatRoom=cls.room1)
        memberInRoom1 = ChatRoomMember.objects.create(
            member=cls.malin, chatRoom=cls.room1
        )
        ChatRoomMessage.objects.create(
            message="Hello from " + cls.fredrika.username,
            member=memberInRoom1,
            chatRoom=cls.room1,
        )

        cls.room2 = ChatRoom.objects.create(name="room2")
        ChatRoomMember.objects.create(member=cls.fredrika, chatRoom=cls.room2)
        memberInRoom2 = ChatRoomMember.objects.create(
            member=cls.kalle, chatRoom=cls.room2
        )
        ChatRoomMessage.objects.create(
            message="Hello from " + cls.kalle.username,
            member=memberInRoom2,
            chatRoom=cls.room2,
        )

        cls.client = APIClient()

    def test_user_part_of_room_can_access_room(self):
        self.client.force_authenticate(user=self.malin)
        response = self.client.get(reverse("room-detail", kwargs={"pk": self.room1.id}))

        self.assertContains(
            response, text=self.room1.name, status_code=status.HTTP_200_OK
        )
        self.assertIn(self.fredrika.pk, response.data["members"])
        self.assertIn(self.malin.pk, response.data["members"])

    def test_user_part_of_room_can_access_room_messages(self):
        self.client.force_authenticate(user=self.malin)
        response = self.client.get(reverse("room-messages-list", args={self.room1.id}))

        message = ChatRoomMessage.objects.filter(chatRoom=self.room1).first()
        self.assertContains(
            response, text=message.message, status_code=status.HTTP_200_OK
        )

    def test_user_not_part_of_room_cannot_access_the_room(self):
        self.client.force_authenticate(user=self.malin)
        response = self.client.get(reverse("room-detail", kwargs={"pk": self.room2.id}))

        self.assertNotContains(
            response, text=self.room2.name, status_code=status.HTTP_404_NOT_FOUND
        )

    def test_user_not_part_of_room_cannot_access_room_messages(self):
        self.client.force_authenticate(user=self.malin)
        response = self.client.get(reverse("room-messages-list", args={self.room2.id}))

        message = ChatRoomMessage.objects.filter(chatRoom=self.room2).first()
        self.assertNotContains(
            response, text=message.message, status_code=status.HTTP_404_NOT_FOUND
        )


class RoomCreationApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.malin = User.objects.create(username="Malin")
        cls.fredrika = User.objects.create(username="Fredrika")
        cls.kalle = User.objects.create(username="kalle")

        cls.client = APIClient()

    def test_user_have_no_rooms_and_creates_a_room(self):
        pass

    def test_user_have_rooms_and_create_a_room(self):
        pass

    def test_user_have_a_room_and_creates_an_identical_room_gets_back_the_original(
        self,
    ):
        pass

    def test_user_tries_to_create_room_with_no_members_gets_error(self):
        pass

    def test_user_tries_to_create_room_with_itself_as_parameter(self):
        pass
