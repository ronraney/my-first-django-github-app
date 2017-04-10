from django.conf.urls import url
from . import views

#Here we are importing Django's function url and all of our views from the blog app

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

#We assign a view called post_list to the ^$URL
#This URL pattern will match ^, a beginning, with $, an end, so only an empty string will match
#The domain, such as 127.0.0.1, or ronraney.com/, are not included
#So the home page will display the views.post_list view
#The name of the URL will be post_list, but this can be different from the name of the view, post_list

