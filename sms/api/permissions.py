# -*- coding: utf8 -*-
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request or not request.user or not request.user.is_authenticated():
            return False
        if not hasattr(obj, 'user'):
            return False
        if getattr(obj, 'user').id == request.user.id:
            return True
