from django.shortcuts import render
from django.views import View
from .models import Blog
# Create your views here.
from .forms import BlogForm, CommentForm

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-created_on')
        form = BlogForm()
        context = {
            'blog_list' : blogs,
            'form' :form,
            'name': request.user
        }

        return render(request, 'blog/blog.html', context)
    def post(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-created_on')
        form = BlogForm(request.POST)

        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()

        context = {
            'blog_list' : blogs,
            'form' :form,
            'name' : request.user.first_name

        }

        return render(request, 'blog/blog.html', context)
        
class BlogDetailView(View):
    def get(self, request,pk, *args, **kwargs):
        blog = Blog.objects.get(pk=pk)
        form = CommentForm()
        context = {
            'blog' : blog,
            'form' : form
        }
        return render(request, 'blog/blog_details.html', context)
        
    
