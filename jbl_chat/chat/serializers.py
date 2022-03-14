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
        fields = ["id", "message", "postedTime", "member"]


class ChatroomSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=User.objects.all()
    )

    class Meta:
        model = ChatRoom
        fields = ["id", "name", "members"]

    def create(self, validated_data):

        members = validated_data.pop("members", [])

        query = ChatRoom.objects.filter(members__id=members.pop().id)
        for member in members:
            query &= ChatRoom.objects.filter(members__id=member.id)

        print(query)
        if query.exists():
            print("ROOM EXISTS----------------------------------------")
            return query.get()

        print("ROOM NOOOO EXISTS----------------------------------------")

        return ChatRoom.objects.create(**validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
