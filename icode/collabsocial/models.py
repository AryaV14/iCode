from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Stacks(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name
class Post(models.Model):
    body = models.TextField()
    # describe the project 
    stacks = models.ManyToManyField(Stacks)
    created_on = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return self.body
