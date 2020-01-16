from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return(render(request,'journal/post_list.html', {'posts':posts}))

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'journal/post_details.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # img = post.upload
            # wpercent = (basewidth / float (img.size [0]))
            # hsize = int ((float (img.size [1]) * float (wpercent)))
            # img = img.resize ((basewidth,hsize), PIL.Image.ANTIALIAS)
            # post.upload = img 
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'journal/post_new.html', {'form': form})

def post_edition (request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'journal/post_new.html', {'form': form})

# $_GET request.GET
# $_POST request.POST

