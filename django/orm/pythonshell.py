"""파이썬 쉘을 사용하기 위한 준비 작업: 웹 앱 설정

1. 웹 앱 생성
명령어: python manage.py makemigrations

===========================================
~/Documents/study/python/django/first-django main*
venv ❯ python manage.py makemigrations
Migrations for 'third':
  third/migrations/0001_initial.py
    - Create model Restaurant
===========================================


2. 1번으로 만든 웹 앱(third)의 third/models.py 파일에서 모델 구현

===========================================
from django.db import models

# Create your models here.


# 모델 구현
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
===========================================

"""


"""파이썬 쉘을 사용하기 위한 준비 작업: 모델 마이그레이션

1. 마이그레이션
생성한 웹 앱(third) migrations 폴더에 0001_initial.py 모델 초기화 파일이 생김
명령어: python manage.py makemigrations

===========================================
~/Documents/study/python/django/first-django main*
venv ❯ python manage.py makemigrations
Migrations for 'third':
  third/migrations/0001_initial.py
    - Create model Restaurant
===========================================


2. 마이그레이트
1번에서 초기화한 파일(0001_initial.py)을 기준으로 db.sqllite3 에 입력됨
명령어: python manage.py migrate

===========================================
~/Documents/study/python/django/first-django main* ⇡
venv ❯ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, second, sessions, third
Running migrations:
  Applying third.0001_initial... OK
===========================================


3. 마이그레이션 적용 현황 보기
명령어: python manage.py showmigrations 앱이름


4. 지정한 마이그레이션의 SQL 내용 보기
명령어: python manage.py sqlmigrate 앱이름 마이그레이션이름


"""
