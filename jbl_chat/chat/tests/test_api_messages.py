from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from chat.models import ChatRoom, ChatRoomMember, ChatRoomMessage
from chat.serializers import ChatRoomMessageSerializer


class MessagesApiTestCase(APITestCase):
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
        cls.room_url = reverse("room-detail", kwargs={"pk": cls.room1.id})
        cls.messages_url = reverse("room-messages-list", args={cls.room1.id})

    def test_messages_are_created_for_active_user(self):
        self.client.force_authenticate(user=self.malin)

        message = "HejHej"

        response = self.client.post(
            reverse("room-messages-list", args={self.room1.id}), {"message": message}
        )

        self.assertContains(response, text=message, status_code=status.HTTP_201_CREATED)
        chatroom_message = ChatRoomMessage.objects.get(message=message)
        serializer = ChatRoomMessageSerializer(chatroom_message)
        self.assertEqual(response.data, serializer.data)

    def test_can_only_post_messages_to_room_user_is_part_of(self):
        self.client.force_authenticate(user=self.malin)

        message = "HejHej"

        response = self.client.post(
            reverse("room-messages-list", args={self.room2.id}), {"message": message}
        )

        self.assertNotContains(
            response, text=message, status_code=status.HTTP_403_FORBIDDEN
        )

    def test_only_messages_belonging_to_room_are_listed(self):
        self.client.force_authenticate(user=self.malin)
        response = self.client.get(reverse("room-messages-list", args={self.room1.id}))

        message_in_room_1 = ChatRoomMessage.objects.filter(chatRoom=self.room1).first()
        self.assertContains(
            response, text=message_in_room_1.message, status_code=status.HTTP_200_OK
        )

        message_in_room_2 = ChatRoomMessage.objects.filter(chatRoom=self.room2).first()
        self.assertNotContains(
            response, text=message_in_room_2.message, status_code=status.HTTP_200_OK
        )

    def test_deleted_messages_are_gone(self):
        self.client.force_authenticate(user=self.malin)

        message_in_room_1 = ChatRoomMessage.objects.filter(chatRoom=self.room1).first()

        response = self.client.delete(
            reverse(
                "room-messages-detail",
                kwargs={"chatRoom_pk": self.room1.id, "pk": message_in_room_1.pk},
            )
        )

        print(response)
        self.assertNotContains(
            response,
            text=message_in_room_1.message,
            status_code=status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(ChatRoomMessage.objects.filter(chatRoom=self.room1).exists())
