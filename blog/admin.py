from django.contrib import admin #We are importing the admin contributable package - the admin interface
from .models import Post #Here we import the Post model from all models

admin.site.register(Post) #This registers our model and makes it visible on the admin page




