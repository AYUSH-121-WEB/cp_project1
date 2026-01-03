from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            post.user = request.user
            post=form.save()
            return redirect('post_list')  # success ke baad
    else:
        form = PostForm()
    return render(request, 'create_post.html' ,{'form': form})

