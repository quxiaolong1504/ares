# -*- coding: utf8 -*-

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from sms.api.serializers import MessageSerializer
from sms.models import Message


class MessageList(ListCreateAPIView):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageDetail(RetrieveAPIView):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    lookup_field = 'id'

    def get_object(self):
        return self.queryset.get(user=self.request.user)
