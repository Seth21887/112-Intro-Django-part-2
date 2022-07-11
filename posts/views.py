from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

# Create your views here.
# We need a HomePageView and an AboutPageView
#Consider: all the different things needed for these to become accessible through our web browser.