from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True)
    is_visible = models.BooleanField(default=False)
    x_coord = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    y_coord = models.DecimalField(max_digits=9, decimal_places=6, null=True)


class Chat(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile1", default=None)
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile2", default=None)
    last_message_sent = models.DateTimeField()


class Message(models.Model):
    text = models.TextField(max_length=512)
    sender_is_profile1 = models.BooleanField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    time_sent = models.DateTimeField()
    time_read = models.DateTimeField()


class Like(models.Model):
    liker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="liker")
    likee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likee")
