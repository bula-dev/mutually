from rest_framework import serializers
from api import models
import datetime
from dateutil.relativedelta import relativedelta

class User(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = ["name", "birthday", "age"]
    
    def get_age(self, obj):
        return relativedelta(datetime.date.today(), obj.birthday).years


class Chat(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = ["user1", "user2"]


class Message(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = ["text", "sender", "chat"]