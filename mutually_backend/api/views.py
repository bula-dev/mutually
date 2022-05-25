from django.shortcuts import render
from api import models, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import IntegrityError



class UserView(APIView):

    def get(self, request):
        """
        For testing.
        """
        users = models.User.objects.all()

        serializer = serializers.User(users, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a user.
        """
        serializer = serializers.User(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()
                token = Token.objects.create(user=user)
                return Response(str(token), status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response(e, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    def get(self, request):
        profiles = models.Profile.objects.all()
        serializer = serializers.Profile(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Create profile"""
        serializer = serializers.Profile(data=request.data)
        print("qweqwe")
        if serializer.is_valid():
            print("***************")
            print(serializer.validated_data)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # {"user": "1", "birthday": "1999-07-20"}
    # name, age, distance
    # {"token": "Token 309c854ef799bf1db2ca35812902d7f2332a9a98",  "user": "2"}
    # {"username": "bula", "password": "123"}


class ChatView(APIView):

    def get(self, request):
        # chats = models.Chat.objects.all(F(user1=request.user) | F(user2=request.user))
        pass

# TODO IS OUTDATED

class LikeView(APIView):

    def get(self, request):
        
        likes = models.Like.objects.all()
        serializer = serializers.Like(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = Token.objects.get(key=request.headers["Autentication"].split(" ")[1]).user
        user2 = models.User.objects.filter(id=request.data["user"])[0]
        print(user2)
        like = models.Like(liker=user,likee=user2)
        like.save()
        return Response(status=status.HTTP_201_CREATED)

        

