from django.db import models

# Create your models here.

# 게시글 남기는 웹 앱
# 장고 모델(models.Model)을 상속받는 Post 클래스 정의
class Post(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()

    # auto_now_add=True : 게시글이 생성될 때 자동으로 현재 시간 기록
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now=True: 현재 시간 기록(수정 시간은 게시글이 생성될 때 기록하는 것이 아니기 때문에 auto_now_add 가 아님)
    updated_at = models.DateTimeField(auto_now=True)

    # num_stars = models.IntegerField() # 별점
