from rest_framework import serializers
from api import models

class User(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ["name", "birthday"]


class Chat(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = ["user1", "user2"]


class Message(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = ["text", "sender", "chat"]