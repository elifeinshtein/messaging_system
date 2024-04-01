from django.contrib.auth.models import User
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer

class MessageView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        messages = Message.objects.filter(receiver=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class UnreadMessageView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        messages = Message.objects.filter(receiver=request.user, is_read=False)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
