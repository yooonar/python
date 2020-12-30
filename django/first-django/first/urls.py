"""각 웹 앱 별 url 설정 파일

firstdjango 폴더 안에 있는 urls.py 에 각 url 설정을 저장하면,
나중에 유지보수 할 때 first 폴더 외에 second, third, .. 각 웹앱 폴더가 생성된다면 문제가 될 수 있다.
같은 페이지 주소지만 웹 앱에 따라 설정이 바뀔 수 있기 때문이다.
그렇기 때문에 각 웹 앱 폴더 사이에 urls.py 파일을 만들어 url 설정을 관리한다.

urlpatterns 을 통해 path 를 정의하면 아래와 같은 형식으로 읽어들인다.
path('select/', views.select, name="select"), -> http(s)://<사이트 도메인>/<웹 앱>/select

- url 중간에 parameter 를 입력받고 싶은 경우
형식: abc.com/select/123/reviews
문법: path('select/<int:year>/reviews', ~~, ~~)

- 정규식 문법을 이용하는 경우 (re_path import 필요!)
형식: /select/2019/
from django.urls import re_path
문법: re_path(r'^select/(?P<year>[0-9]{4}/$)') <- 숫자 4자리, / 로 끝남
"""

from django.urls import path

# 같은 경로에 있는 first/views 호출
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # name="select" 으로 선언하면 뷰 페이지에서 {% url 'select' %} 와 같은 형식으로 사용 가능하다.
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),
]
