from django.urls import path

# 같은 경로에 있는 second/views 호출
from . import views

urlpatterns = [
    path('list/', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('confirm/', views.confirm, name="confirm"),
]
