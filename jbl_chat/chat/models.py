from email import message
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.


class TrackabelModel(models.Model):

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChatRoom(TrackabelModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    members = models.ManyToManyField(
        User, related_name="chatrooms", through="ChatRoomMember"
    )

    def __str__(self):
        return self.name


# I made a custom MTM-through-table since we might need extra fields
# and it is difficult to add a through-table after the database is created
class ChatRoomMember(TrackabelModel):

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        return "{} @ {}".format(self.member.__str__(), self.chatRoom.__str__())


class ChatRoomMessage(TrackabelModel):

    message = models.TextField()
    member = models.ForeignKey(ChatRoomMember, on_delete=models.PROTECT)
    chatRoom = models.ForeignKey(
        ChatRoom, related_name="messages", on_delete=models.CASCADE
    )
