from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    print form
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, 'Your Post Was Successfully Created')
        return redirect('list')
    cxt = {'form': form}
    return render(request, 'post_form.html', cxt)
    
    
def post_detail(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    cxt = {'title': post.title, 'post': post}
    return render(request, 'post_detail.html', cxt)
    
    
def post_list(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    cxt = {'posts': posts, 'title': 'Post List. .'}
    return render(request, 'post_list.html', cxt)
    
    
def post_update(request, pk=None):
    obj = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    cxt = {'form': form}
    return render(request, 'post_form.html', cxt)            
    
    
def post_delete(request, pk=None):
    obj = get_object_or_404(Post, pk=pk)
    obj.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('list')

