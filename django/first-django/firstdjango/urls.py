"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 프로젝트 전체에 관한 설정 - startproject 명령어로 생성된 파일(명령어: `django-admin startproject firstdjango .`)
# url 관련 규칙 파일

from django.contrib import admin
from django.urls import path, include
from first import views # first 안에 있는 views.py 를 가져와 맵핑

urlpatterns = [
    path('admin/', admin.site.urls),

    # 프로젝트 공통 url 설정
    # path('', views.index, name='index'), # 인덱스 페이지에서는 views.py > index() 메소드가 제공하는 응답 값으로 제공하겠다.

    # 각 웹 앱 별 url 설정 파일 include - first 웹 앱
    path('first/', include('first.urls')),

    # 각 웹 앱 별 url 설정 파일 include - second 웹 앱
    path('second/', include('second.urls')),

    # 각 웹 앱 별 url 설정 파일 include - third 웹 앱
    path('third/', include('third.urls')),

]
