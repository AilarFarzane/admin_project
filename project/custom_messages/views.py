from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Message
from .serializers import MessageSerializer
user = get_user_model()



class MessageList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, sender_id=None, *args, **kwargs):
        # if the user_id is provided filter the messages by the user ID, if not list all messages
        sender_id = request.query_params.get('sender_id')
        if sender_id:
            messages = Message.objects.filter(sender_id=sender_id)
            if not messages.exists():
                return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            messages = Message.objects.all()

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs): #create a new message
        data = request.data.copy()
        data['sender'] = request.user.id
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MessageDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs): #details of a single Message
        message = get_object_or_404(Message, pk=pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)








