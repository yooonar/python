from django.urls import path
from . import views

# 템플릿에서 구분지을 수 있도록 앱 이름을 지정함
app_name = 'polls'

urlpatterns = [
    # 메인 페이지 /polls/
    path('', views.index, name='index'),
    # 상세 페이지 /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 결과 페이지 /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 투표 페이지 /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
