from rest_framework import serializers
from api import models
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class Profile(serializers.ModelSerializer):

    #age = serializers.SerializerMethodField()
    #username = serializers.StringRelatedField(source="user")
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, source="user")

    class Meta:
        model = models.Profile
        fields = ["birthday",  "user_id"]
    
    def get_age(self, obj):
        return relativedelta(datetime.date.today(), obj.birthday).years


class User(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "password", "token"]

    def get_token(self, obj):
        return str(Token.objects.filter(user=obj)[0])


class Chat(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = ["profile1", "profile2"]


class Like(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = ["liker", "likee"]


class Message(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = ["text", "sender", "chat"]