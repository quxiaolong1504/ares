# -*- coding: utf8 -*-

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from sms.api.permissions import IsOwner
from sms.api.serializers import MessageSerializer
from sms.models import Message
from utils.responses import HttpResponseDeleted


class MessageList(ListCreateAPIView):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_del=0)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).all()


class MessageDetail(RetrieveDestroyAPIView):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Message.objects.all()
    lookup_field = 'id'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg], 'is_del': 0}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_del = True
        instance.save()
        return HttpResponseDeleted()


