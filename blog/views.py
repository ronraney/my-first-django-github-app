from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #This creates a variable called posts which holds our query set
    return render(request, 'blog/post_list.html', {'posts': posts})
    #The last part {} adds some things for the template to use - i.e. the variable created above