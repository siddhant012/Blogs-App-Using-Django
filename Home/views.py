from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from . models import Post

class PostListView(ListView):
    model = Post
    template_name='Home/home.html'
    context_object_name='posts'
    ordering='-date_posted'
    paginate_by=2

    #return HttpResponse('<h1>some heading</h1>')


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model=Post
    template_name='Home/post_create_update.html'
    fields=['title','content']
    success_message='Post created successfully'
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model=Post
    template_name='Home/post_detail.html'
    fields=['author','title','content','date_posted']
    context_object_name='post'


class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    template_name='Home/post_create_update.html'
    fields=['title','content']
    success_message='Post updated successfully'
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False

class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    template_name='Home/post_delete.html'
    context_object_name='post'
    success_url='/'
    success_message='Post deleted successfully'

    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False

