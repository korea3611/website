from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.core.paginator import Paginator

from django.contrib import messages
from django.db.models import Q


# Create your views here.



def index(request):
    blogs = Post.objects
    blog_list = Post.objects.all()
    paginator = Paginator(blog_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'board/base.html', {'blogs':blogs, 'posts':posts})


    


class UploadView(CreateView):
    model = Post
    fields = ['author','OS','title','photo','text']
    template_name = 'board/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})


class DetailView(generic.DetailView):
    model = Post
    template_name = 'board/detail.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'board/delete.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['OS', 'title', 'photo', 'text']
    template_name = 'board/update.html'




