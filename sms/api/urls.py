# -*- coding: utf8 -*-

from django.conf.urls import url
from handlers import MessageList, MessageDetail

urlpatterns = [
    url(r'^$', MessageList.as_view()),
    url(r'^(?P<id>\d+)/$', MessageDetail.as_view()),
]
