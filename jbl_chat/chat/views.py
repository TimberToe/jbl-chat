from django.contrib.auth.models import User, Group
from chat.models import ChatRoom, ChatRoomMember, ChatRoomMessage
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    ChatRoomMemberSerializer,
    UserSerializer,
    GroupSerializer,
    ChatroomSerializer,
    ChatRoomMessageSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id).order_by("username")


class ChatRoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows chatrooms to be viewed or edited.
    """

    serializer_class = ChatroomSerializer

    def get_queryset(self):
        return ChatRoom.objects.filter(members__exact=self.request.user.id)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChatRoomMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ChatRoomMembers to be viewed or edited.
    """

    queryset = ChatRoomMember.objects.all()
    serializer_class = ChatRoomMemberSerializer


class ChatRoomMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ChatRoomMessage to be viewed or edited.
    """

    serializer_class = ChatRoomMessageSerializer

    def get_queryset(self):
        return ChatRoomMessage.objects.filter(chatRoom=self.kwargs["chatRoom_pk"])

    def perform_create(self, serializer):

        serializer.save(
            chatRoom=ChatRoom.objects.get(pk=self.kwargs["chatRoom_pk"]),
            member=ChatRoomMember.objects.get(
                member=self.request.user.id, chatRoom=self.kwargs["chatRoom_pk"]
            ),
        )
