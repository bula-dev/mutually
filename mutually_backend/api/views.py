from django.shortcuts import render
from api import models, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserView(APIView):

    def get(self, request):
        users = models.User.objects.all()

        serializer = serializers.User(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.User(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # name, age, distance


class ChatView(APIView):

    def get(self, request):
        # chats = models.Chat.objects.all(F(user1=request.user) | F(user2=request.user))
        pass



