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


"""파이썬 쉘로 진입하여 임시 데이터 입력

1. 파이썬 쉘 접근
명령어: python manage.py shell

===========================================
~/Documents/study/python/django/first-django main* ⇡
venv ❯ python manage.py shell
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
===========================================


2. 모델 import 하기
쉘을 닫았다 다시 열 때마다 초기화 되기 때문에 쉘을 열 때마다 import 해준다.
명령어: from 웹앱명.models import 모델클래스명

===========================================
>>> from third.models import Restaurant
>>>
===========================================


3. 임시 데이터 입력하기
데이터 입력해줌
명령어: 모델클래스명(컬럼명="정보").save()

===========================================
>>> Restaurant(name="Deli Shop", address="Gangnam").save()
>>> Restaurant(name="Korean food", address="Gangbuk").save()
>>> Restaurant(name="Sushi", address="Gangbuk").save()
===========================================


4. 3번에서 저장한 데이터(이하 object) 전체 정보 가져오기
명령어: object명.objects.all()

===========================================
>>> Restaurant.objects.all()
<QuerySet [<Restaurant: Restaurant object (1)>, <Restaurant: Restaurant object (2)>, <Restaurant: Restaurant object (3)>]>
===========================================

"""

"""파이썬 쉘로 데이터 조회, 필터링

1. 전체 정보 가져오기
명령어: object명.objects.all()

===========================================
>>> Restaurant.objects.all()
<QuerySet [<Restaurant: Restaurant object (1)>, <Restaurant: Restaurant object (2)>, <Restaurant: Restaurant object (3)>]>
===========================================


2. get 명령어로 특정 조건의 정보만 가져오기
리턴 타입은 String, Int 등이다.
명령어: object명.objects.get(조건).컬럼명

===========================================
>>> Restaurant.objects.get(pk=1).name
'Deli Shop'
===========================================


3. filter 명령어로 특정 조건의 값 가져오기
리턴 타입은 QuerySet 이다.
명령어: object명.objects.filter(조건=값).values()

===========================================
>>> Restaurant.objects.filter(name='Deli Shop').values()
<QuerySet [{'id': 1, 'name': 'Deli Shop', 'address': 'Gangnam', 'create_at': datetime.datetime(2021, 1, 3, 12, 55, 54, 118109, tzinfo=<UTC>), 'update_at': datetime.datetime(2021, 1, 3, 12, 55, 54, 118162, tzinfo=<UTC>)}]>
===========================================


4. exclude 명령어로 특정 조건을 제외한 값 가져오기
리턴 타입은 QuerySet 이다.
명령어: object명.objects.exclude(조건=값).values()

===========================================
>>> Restaurant.objects.exclude(name='Deli Shop').values()
<QuerySet [{'id': 2, 'name': 'Korean food', 'address': 'Gangbuk', 'create_at': datetime.datetime(2021, 1, 3, 12, 56, 10, 915980, tzinfo=<UTC>), 'update_at': datetime.datetime(2021, 1, 3, 12, 56, 10, 916014, tzinfo=<UTC>)}, {'id': 3, 'name': 'Sushi', 'address': 'Gangbuk', 'create_at': datetime.datetime(2021, 1, 3, 12, 56, 29, 773010, tzinfo=<UTC>), 'update_at': datetime.datetime(2021, 1, 3, 12, 56, 29, 773048, tzinfo=<UTC>)}]>
===========================================

"""


"""파이썬 쉘로 페이징, 정렬하기

1. 페이징하기(0 ~ 9까지의 데이터 가져오기)
0번지부터 10번지 전(9번지)까지 가져오기
명령어: object명.objects.all()[페이징시작값:페이징끝값]

===========================================
>>> Restaurant.objects.all()[0:10]
<QuerySet [<Restaurant: Restaurant object (1)>, <Restaurant: Restaurant object (2)>, <Restaurant: Restaurant object (3)>]>
===========================================


2. 생성순으로 정렬하기
생성일 오름차순으로 정렬하기
명령어: object명.objects.order_by('날짜컬럼명')

===========================================
>>> Restaurant.objects.order_by('create_at')
<QuerySet [<Restaurant: Restaurant object (1)>, <Restaurant: Restaurant object (2)>, <Restaurant: Restaurant object (3)>]>
===========================================


3. 최신순으로 정렬하기
생성일 내림차순으로 정렬하기
명령어: obejct명.objects.order_by('-날짜컬럼명')

===========================================
>>> Restaurant.objects.order_by('-create_at')
<QuerySet [<Restaurant: Restaurant object (3)>, <Restaurant: Restaurant object (2)>, <Restaurant: Restaurant object (1)>]>
===========================================


4. 최신순 정렬 후 페이징한 정보 가져오기
쉘로 입력한 데이터가 별로 없어 3개의 데이터만 가져온다.
명령어: object명.objects.order_by('날짜컬럼명')[페이징시작값:페이징끝값].values()

===========================================
>>> Restaurant.objects.order_by('-create_at')[1:3].values()
<QuerySet [{'id': 2, 'name': 'Korean food', 'address': 'Gangbuk', 'create_at': datetime.datetime(2021, 1, 3, 12, 56, 10, 915980, tzinfo=<UTC>), 'update_at': datetime.datetime(2021, 1, 3, 12, 56, 10, 916014, tzinfo=<UTC>)}, {'id': 1, 'name': 'Deli Shop', 'address': 'Gangnam', 'create_at': datetime.datetime(2021, 1, 3, 12, 55, 54, 118109, tzinfo=<UTC>), 'update_at': datetime.datetime(2021, 1, 3, 12, 55, 54, 118162, tzinfo=<UTC>)}]>
===========================================

"""