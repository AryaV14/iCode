from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    body = models.TextField()
    # describe the project 
    stacks = models.TextField()
    created_on = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
