import datetime

from django.test import TestCase
from django.utils import timezone
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
