# Generated by Django 3.2.8 on 2022-03-13 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20220312_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroommessage',
            name='chatRoom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chatroom'),
        ),
    ]
