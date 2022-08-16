from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


# Create your views here.
def index(request):
    # 일자를 기준으로 5개까지만 가져옴
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    '''
    # 템플릿 형식으로 변경하여 사용하지 않음!

    # 투표 질문 리스트를 콤마로 구분하여 보여줌
    # What's your favorite food to eat?, What's new? 이런 식으로!
    output = ', '.join([q.question_text for q in latest_question_list])
    
    return HttpResponse(output)
    '''

    # 템플릿에 데이터를 전달함
    context = {
        'latest_question_list': latest_question_list,
    }

    # 1. HttpResponse를 이용한 방법
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # 2. render를 이용한 방법
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse('You\'re looking at question %s.' % question_id)


def results(request, question_id):
    response = 'You\'re looking at the results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)
