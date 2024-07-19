from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView,
                                   CreateView, UpdateView,
                                   DeleteView)
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, "blog/home.html", context)

# using class based views instead of the above function based
class PostlistView(ListView):
    model = Post

    #setting the template to use <app>/><model>_<viewtype>.html
    template_name = 'blog/home.html'

    #setting the class to loop over posts instead of defaul object lists
    context_object_name = 'posts'

    #order the posts with dates. adding - sign to start from latest
    ordering = ['-date_posted']

    #introucing pagination
    paginate_by = 10


#viewing the user details
class UserPostlistView(ListView):
    model = Post

    #setting the template to use <app>/><model>_<viewtype>.html
    template_name = 'blog/user_post.html'

    #setting the class to loop over posts instead of defaul object lists
    context_object_name = 'posts'

    #order the posts with dates. adding - sign to start from latest
    ordering = ['-date_posted']

    #introucing pagination
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))

        return Post.objects.filter(author = user).order_by('-date_posted')
        

#creating post details using class view

class PostDetailView(DetailView):
    model = Post


#creating class to allow class to create a new post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    #setting the author
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
    
#creating an update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    #setting the author
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
    
    #creating method to see if a user passes 
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


#add about about page
def about(request):
    return render(request, "blog/about.html", {'title': 'About'})