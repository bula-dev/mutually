from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    x_coord = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    y_coord = models.DecimalField(max_digits=9, decimal_places=6, null=True)



class Chat(models.Model):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile1")
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile2")
    last_message_sent = models.DateTimeField()


class Message(models.Model):
    text = models.TextField(max_length=512)
    sender_is_chat_user1 = models.BooleanField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    time_sent = models.DateTimeField()
    time_read = models.DateTimeField()


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    likee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likee")
