from django.contrib import admin
from .models import Post,Stacks
# Register your models here.


admin.site.register([Stacks,Post])