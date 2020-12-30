"""각 웹 앱 별 url 설정 파일

firstdjango 폴더 안에 있는 urls.py 에 각 url 설정을 저장하면,
나중에 유지보수 할 때 first 폴더 외에 second, third, .. 각 웹앱 폴더가 생성된다면 문제가 될 수 있다.
같은 페이지 주소지만 웹 앱에 따라 설정이 바뀔 수 있기 때문이다.
그렇기 때문에 각 웹 앱 폴더 사이에 urls.py 파일을 만들어 url 설정을 관리한다.
"""

from django.urls import path

# 같은 경로에 있는 first/views 모델 호출
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]