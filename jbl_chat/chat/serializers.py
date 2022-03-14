from django.contrib.auth.models import User, Group
from rest_framework import serializers
from chat.models import ChatRoom, ChatRoomMember, ChatRoomMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class ChatRoomMemberSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="member.id")
    name = serializers.ReadOnlyField(source="member.username")

    class Meta:
        model = ChatRoomMember
        fields = ["id", "name"]


class ChatRoomMessageSerializer(serializers.ModelSerializer):
    member = ChatRoomMemberSerializer(read_only=True)

    class Meta:
        model = ChatRoomMessage
        fields = ["message", "postedTime", "member"]


class ChatroomSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, 
    read_only=False,
    queryset=User.objects.all())

    class Meta:
        model = ChatRoom
        fields = ["id", "name", "members"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
