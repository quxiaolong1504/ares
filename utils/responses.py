# -*- coding: utf8 -*-
from django.http import HttpResponse


class HttpResponseDeleted(HttpResponse):
    status_code = 204

