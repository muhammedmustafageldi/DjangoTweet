from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=140)
    time = models.CharField(max_length=20, null=True)
    time_unix = models.BigIntegerField(null=True)


    def __str__(self):
        return f"Nickname: {self.username}, Tweet: {self.body}, Time: {self.time}"