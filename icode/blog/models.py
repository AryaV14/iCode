from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    body = models.TextField()
    # describe the project 
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return (self.body)

class Comments(models.Model):
    body = models.TextField()
    # describe the project 
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
