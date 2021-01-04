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
