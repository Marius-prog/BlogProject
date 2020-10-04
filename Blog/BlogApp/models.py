from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    tittle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.tittle + " | " + str(self.author)

# Create your models here.
