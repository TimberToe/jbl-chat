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

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows chatrooms to be viewed or edited.
    """

    queryset = ChatRoom.objects.all().order_by("create_date")
    serializer_class = ChatroomSerializer


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

    queryset = ChatRoomMessage.objects.all()
    serializer_class = ChatRoomMessageSerializer
