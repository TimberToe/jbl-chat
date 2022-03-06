from email import message
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

User = get_user_model()

# Create your models here.


class TrackabelModel(models.Model):

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def _generate_unique_uri():
    """Generates a unique uri for the chat session."""
    return str(uuid4()).replace("-", "")[:15]


class ChatRoom(TrackabelModel):

    guid = models.URLField(default=_generate_unique_uri)


class ChatRoomMember(TrackabelModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ChatRoomMessage(TrackabelModel):

    message = models.TextField()
    user = models.ForeignKey(ChatRoomMember, on_delete=models.PROTECT)
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
