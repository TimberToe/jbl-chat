from django.contrib.auth.models import User, Group
from rest_framework import serializers
from chat.models import ChatRoom, ChatRoomMember, ChatRoomMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class ChatRoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomMember
        fields = ["member", "chatRoom"]


class ChatRoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomMessage
        fields = ["message", "member"]


class ChatroomSerializer(serializers.ModelSerializer):
    messages = ChatRoomMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ["id", "name", "messages"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
