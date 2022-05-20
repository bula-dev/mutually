from rest_framework import serializers
import models


class User(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = []


class Chat(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = []


class Message(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = []