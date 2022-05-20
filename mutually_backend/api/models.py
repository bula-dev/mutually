from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateField()


class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    text = models.TextField(max_length=512)
    sender = models.BooleanField()
    chat = models.ForeignKey(Chat)
    time_sent = models.DateTimeField()
    time_read = models.DateTimeField()





