from django.shortcuts import render
from django.views import View
from .models import Post
# Create your views here.
from .forms import PostForm

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        context = {
            'post_list' : posts,
            'form' :form,
            'name': request.user
        }

        return render(request, 'collabsocial/collab.html', context)
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list' : posts,
            'form' :form,
            'name' : request.user.first_name

        }

        return render(request, 'collabsocial/collab.html', context)
        
class PostDetailView(View):
    def get(self, request,pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        context = {
            'post' : post
        }
        return render(request, 'collabsocial/post_details.html', context)
      
    
