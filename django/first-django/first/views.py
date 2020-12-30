# 각 프로젝트 별 설정 - startapp 명령어로 생성된 파일(명령어: `python3 manage.py startapp first`)
# 백엔드 코드를 정의하고 구현하는 파일(데이터 처리 구현)
"""django.shortcuts 를 import 하면?

각 메소드별로 template = loader.get_template('index.html') 를 생략할 수 있다.
"""
from django.shortcuts import render
from django.http import HttpResponse

# templates/index.html 파일을 로딩해 response 로 돌려줌
from django.template import loader

# 시간 출력
from datetime import datetime


# Create your views here.
# view 파일에서는 기본적으로 index 를 정의하면 request(object) 를 받을 수 있다.
def index(request):
    # loader.get_template('파일명') <- 템플릿 호출
    # django.shortcuts 으로 선언 생략 가능
    # template = loader.get_template('index.html')

    # 현재 시간 출력
    now = datetime.now()

    # 동적으로 변수 삽입(렌더링 할 떄 사용)
    context = {
        'current_date': now, # 현재 시간
    }

    # template.render(context, request) <- 템플릿 렌더링
    # django.shortcuts 으로 선언 생략 가능
    # return HttpResponse(template.render(context, request))
    return render(request, 'first/index.html', context)


def select(request):
    message = "수 하나를 입력해주세요."
    context = {
        'number': 3,
    }

    # return HttpResponse(message)
    return render(request, 'first/select.html', context)


def result(request):
    message = "추첨 결과입니다."
    context = {
        'numbers': [1, 2, 3, 4, 5, 6],
    }

    # return HttpResponse(message)
    return render(request, 'first/result.html', context)
