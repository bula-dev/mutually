from django.shortcuts import render
import api.models
import api.serializers
from rest_framework.response import Response



class UserView():

    def get(self, request):
        user = models.User.objects.all()

        serializer = serialiers.User(model=models.User, many=True)
        return Response(serializer.data)

    # name, age, distance


class ChatView():

    def get(self, request):
        # chats = models.Chat.objects.all(F(user1=request.user) | F(user2=request.user))
        pass



