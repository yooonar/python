from django.urls import path
from . import views

# 템플릿에서 구분지을 수 있도록 앱 이름을 지정함
app_name = 'polls'

# 제네릭 뷰(generic view) 사용
urlpatterns = [
    # 메인 페이지 /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # 상세 페이지 /polls/1/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),

    # 결과 페이지 /polls/1/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # 투표 페이지 /polls/1/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
