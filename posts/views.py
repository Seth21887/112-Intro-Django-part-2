from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView): #the way to read this is PostDetailView is extending the DetailView class
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "body"]

# Create your views here.
# We need a HomePageView and an AboutPageView
#Consider: all the different things needed for these to become accessible through our web browser.