# Generated by Django 3.2.8 on 2022-03-12 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_room_chatroommember_chatroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroommember',
            old_name='user',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='chatroommessage',
            old_name='user',
            new_name='member',
        ),
    ]
