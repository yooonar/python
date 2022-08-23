from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # , Http404
from .models import Question, Choice
from django.urls import reverse
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
    # 1. HttpResponse를 이용한 방법
    # return HttpResponse('You\'re looking at question %s.' % question_id)

    # 1) try, except를 이용해 404 페이지 예외 처리
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")

    # 2) 숏컷에 있는 get_object_or_404를 이용해 404 페이지 예외 처리
    question = get_object_or_404(Question, pk=question_id)
    # 2. render를 이용한 방법
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = 'You\'re looking at the results of question %s.'
    # return HttpResponse(response % question_id)

    # 넘겨받은 question_id를 통해 question 데이터 조회
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # question_id 를 넘겨받아 데이터를 조회
    question = get_object_or_404(Question, pk=question_id)

    try:
        # question에 대해 외래키를 갖는 선택지를 가져온다.
        # request.POST['choice_id'] = 템플릿에서 넘겨받은 input 값의 이름
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # selected_choice 가 없는 경우 except 문을 탐
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
          'question': question,
          'error_message': "You didn't select a choice.",
        })

    # selected_choice 가 있는 경우 아래를 실행
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # post로 호출된 경우는 HttpResponseRedirect 로 페이지 이동
        # reverse 는 페이지 이동할 때 하드코딩 하지 않고 이동할 수 있도록 사용한 것
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    # return HttpResponse('You\'re voting on question %s.' % question_id)
