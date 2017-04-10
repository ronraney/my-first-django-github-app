from django.db import models
from django.utils import timezone

#These lines add bits from other files - like the models class and the timezone utility

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self): #This is the publish method for the post - def means that it is a function/method - lowercase is used
        self.published_date = timezone.now() 
        self.save()
        
    def __str__(self):
        return self.title
#This is an example of a method returning something, i.e. the title of the Post

#####What's going on here?######

#Creating a model, or object, called Post with a bunch of fields (Always use uppercase with Model names)

###Each model is a Python class that subclasses django.db.models.Model
###Each attribute of the model represents a database field, and can be called properties
###Each attribute is a class(Post) attribute and a sort of variable
###Each field should be an instance of an appropriate Field class, such as CharField, TextField, or a widget

#There are dozens of built-in fields that make life easier, but you can create your own
#Fields take on arguments, e.g. the CharField field has the max_length argument
