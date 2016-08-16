from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Friendship(models.Model):
    person = models.ForeignKey(Person, related_name="friend1")
    friend = models.ForeignKey(Person, related_name="friend2")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
