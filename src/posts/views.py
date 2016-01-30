from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        return redirect(reverse('list'))
    cxt = {'form': form}
    return render(request, 'post_form.html', cxt)
    
    
def post_detail(request, pk=None):
    obj = get_object_or_404(Post, pk=pk)
    cxt = {'title': obj.title, 'obj': obj}
    return render(request, 'post_detail.html', cxt)
    
    
def post_list(request):
    queryset = Post.objects.all()
    cxt = {'object_list': queryset, 'title': 'List'}
    return render(request, 'index.html', cxt)
    
    
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
    pass

