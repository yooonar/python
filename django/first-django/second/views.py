from django.shortcuts import render

from second.models import Post

# django 기본 폼 가져오기
from .forms import PostForm

# Create your views here.

def list(request) :
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request) :
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})