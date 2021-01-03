from django.shortcuts import render

from second.models import Post

# 리다이렉트 import
from django.http import HttpResponseRedirect

# django 기본 폼 가져오기
from .forms import PostForm

# Create your views here.


def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    # POST 전송인 경우 유효성 체크
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # 레코드를 생성하는 코드가 필요함
            print(form)
        # 유효성 체크가 안된 경우 목록 페이지로 이동시킴
        return HttpResponseRedirect('/second/list/')

    # GET 전송인 경우 폼 양식과 함께 create 페이지가 노출됨
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    # object 생성자를 넘기면 자동으로 맵핌됨
    form = PostForm(request.POST)

    # 폼 유효성 체크
    if form.is_valid():
        return render(request, 'second/confirm.html', {'form': form})

    # 유효성 체크에 실패하면 다시 입력창으로 이동
    return HttpResponseRedirect('/create/')
