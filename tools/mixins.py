from django.db import models


class DateTimeMixin(object):
    def __init__(self):
        pass

    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
