import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question


# 테스트 파일명은 test.py, 함수 이름은 test_ 로 시작해야 함
# Create your tests here.
class QuestionModelTests(TestCase):

    # 1일이 넘어갈 때에 대한 결과값이 False가 나와야 함
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # 1일이 넘어가지 않았을 때에 대한 결과값이 True가 나와야 함
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        # 미래(30일 후) 데이터를 입력해도 최근 데이터라고 출력되는지 테스트하는 코드
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        # 미래에 대한 글을 입력했을 때 원하는 값(False)이 나오는지 테스트
        # 실행할 콘솔 명령어: py manage.py test polls
        self.assertIs(future_question.was_published_recently(), False)

        """
        수정 전 실행 결과
        Traceback (most recent call last):
          File "d:\R\workspace\python\django\mysite\polls\tests.py", line 20, in test_was_published_recently_with_future_question
            self.assertIs(future_question.was_published_recently(), False)
        AssertionError: True is not False
        
        ----------------------------------------------------------------------
        Ran 1 test in 0.001s
        
        FAILED (failures=1)
        Destroying test database for alias 'default'...

        수정 후 실행 결과
        Ran 1 test in 0.000s
        
        OK
        Destroying test database for alias 'default'...
        """


# 테스트 데이터를 만들기 위한 함수
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    # 데이터가 없는 경우
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        # assertEqual 같은 데이터인지 비교하는 경우
        self.assertEqual(response.status_code, 200)
        # assertContains 포함되어 있는지 확인하는 경우
        self.assertContains(response, "No polls are available.")
        # assertQuerysetEqual Queryset인 경우
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 데이터가 과거인 경우, 데이터가 나오지 않으면 문제가 있는 것!
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],  # 데이터가 있는지 확인
        )

    # 데이터가 미래인 경우, 데이터가 나오면 문제가 있는 것!
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])  # 데이터가 비어있는지 확인

    # 데이터가 과거 1, 미래 1 인 경우, 과거 데이터만 나와야 정상! 미래 데이터가 나오면 문제 있는 것!
    def test_future_question_and_past_question(self):
        question1 = create_question(question_text="Past question.", days=-30)
        question2 = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question1]  # 과거 데이터만 나오는지 확인
        )

    # 데이터가 과거 2인 경우, 2개의 데이터가 나와야 정상!
    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1]  # 과거 데이터가 두개 나오는지 확인
        )

    """
    indexView test 실행 결과
    Ran 8 tests in 0.015s
    
    OK
    Destroying test database for alias 'default'...
    """
