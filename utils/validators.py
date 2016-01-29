# -*- coding: utf8 -*-
import re

from rest_framework.exceptions import ValidationError


class Phone(object):
    """Validate an Phone in China.

    :param str error: Error message to raise in case of a validation error. Can be
        interpolated with `{input}`.
    """

    PHONE_REGEX = re.compile(r"^\d{6,20}$")

    default_message = '{input} is not a valid phone.'

    def __init__(self, error=None):
        self.error = error or self.default_message

    def _format_error(self, value):
        return self.error.format(input=value)

    def __call__(self, value):
        message = self._format_error(value)

        if not value or len(value) != 11:
            raise ValidationError(message)

        if not self.PHONE_REGEX.match(value):
            raise ValidationError(message)
        return value