from rest_framework import serializers
from api import models
import datetime
from dateutil.relativedelta import relativedelta

class Profile(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()
    #user = serializers.StringRelatedField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Profile
        fields = ["user", "age"]
    
    def get_age(self, obj):
        return relativedelta(datetime.date.today(), obj.birthday).years


class Chat(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = ["user1", "user2"]

class Like(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = ["liker", "likee"]


class Message(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = ["text", "sender", "chat"]