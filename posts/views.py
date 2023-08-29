from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # If the form is vailid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')

            # No, Show error
        else:
            return HttpResponseRedirect(form.errors.as_json())


    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    context = {
        'posts': posts,

    }
    # Show post template
    return render(request, 'posts.html', context=context)

def delete(request, post_id):
    # Find post id
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    # Find post id
    posts = Post.objects.get(id = post_id)
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
                # No, Show error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'edit.html', context = {'posts': posts, 'form': form,})

# def post_likes(request):
#     if request.method == 'POST':
#         d