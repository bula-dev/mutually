from django.shortcuts import render
from api import models, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserView(APIView):

    def get(self, request):
        profiles = models.Profile.objects.all()

        serializer = serializers.Profile(profiles, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a user.
        """
        user = User.objects.create_user(request.data["username"], request.data["password"]) 
        user.save()
        token = Token.objects.create(user=user)
        print(token.key)
        profile = models.Profile(user=user, birthday=request.data["birthday"])
        profile.save()
        return Response(token.key, status=status.HTTP_201_CREATED)



    # {"username": "Buh La", "password": "Håkan", "birthday": "1999-07-20"}
    # name, age, distance
    # {"token": "Token 309c854ef799bf1db2ca35812902d7f2332a9a98",  "user": "2"}


class ChatView(APIView):

    def get(self, request):
        # chats = models.Chat.objects.all(F(user1=request.user) | F(user2=request.user))
        pass



class LikeView(APIView):

    def get(self, request):
        
        likes = models.Like.objects.all()
        serializer = serializers.Like(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = Token.objects.get(key=request.data["token"].split(" ")[1]).user
        user2 = models.User.objects.filter(id=request.data["user"])[0]
        print(user2)
        like = models.Like(liker=user,likee=user2)
        like.save()
        return Response(status=status.HTTP_201_CREATED)

        

