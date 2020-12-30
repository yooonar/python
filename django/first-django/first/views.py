# 각 프로젝트 별 설정 - startapp 명령어로 생성된 파일(명령어: `python3 manage.py startapp first`)
# 백엔드 코드를 정의하고 구현하는 파일(데이터 처리 구현)
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# view 파일에서는 기본적으로 index 를 정의하면 request(object) 를 받을 수 있다.
def index(request):
    return HttpResponse("Hello World~!")


def select(request):
    message = "수 하나를 입력해주세요."
    return HttpResponse(message)


def result(request):
    message = "추첨 결과입니다."
    return HttpResponse(message)
