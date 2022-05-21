from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateField()
    x_coord = models.DecimalField(max_digits=9, decimal_places=6)
    y_coord = models.DecimalField(max_digits=9, decimal_places=6)


class Chat(models.Model):
    user1 = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(to=User, on_delete=models.CASCADE)
    last_message_sent = models.DateTimeField()


class Message(models.Model):
    text = models.TextField(max_length=512)
    sender = models.BooleanField()
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE)
    time_sent = models.DateTimeField()
    time_read = models.DateTimeField()







