from django.db import models


class Room(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Message(models.Model):
  value = models.CharField(max_length=255)
  date = models.DateTimeField(auto_now_add=True)
  user = models.CharField(max_length=255)
  room = models.CharField(max_length=255)