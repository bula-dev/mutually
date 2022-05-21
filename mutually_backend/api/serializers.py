from rest_framework import serializers
import api.models


class User(serializers.ModelSerializer):

    class Meta:
        model = api.models.User
        fields = ["name", "birthday"]


class Chat(serializers.ModelSerializer):

    class Meta:
        model = api.models.Chat
        fields = ["user1", "user2"]


class Message(serializers.ModelSerializer):

    class Meta:
        model = api.models.Message
        fields = ["text", "sender", "chat"]