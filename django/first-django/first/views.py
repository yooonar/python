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

import random


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
    # 사용자 입력 값 <- get 으로 넘어온 number 값은 str 형식이기 때문에 int 형식으로 변환해준다.(범위 비교해야해서)
    chosen = int(request.GET['number'])

    results = []
    # 입력받은 number 값 필수로 넣기
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    # 0 ~ 45 사이의 난수를 box 배열에 넣기
    box = []
    for i in range(0, 45):
        # 사용자가 입력한 값은 넣지 않는 조건 추가
        if chosen != i + 1:
            box.append(i + 1)

    # 배열 섞기
    random.shuffle(box)

    # box 에서 하나씩 꺼내기
    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results,
    }

    # return HttpResponse(message)
    return render(request, 'first/result.html', context)
