from django import forms

# ModelForm 은 Model 을 사용하기 때문에 models 도 같이 import 해야함
from django.forms import ModelForm
from second.models import Post

"""gettext_lazy

다국어 설정 등을 위해 맵핑 기능
기존 사용 방식은 gettext_lazy('') 이지만 
gettext_lazy as _ 로 치환해주었기 때문에 _('') 로 사용이 가능하다.
"""
from django.utils.translation import gettext_lazy as _

"""
이렇게 각각 생성하면 필드가 변경될 때마다 form.py, models.py 에 중복된 코드를 넣어줘야 한다.
너무 번거로운 작업이기 때문에 한 번에 처리할 수 있도록 장고에서 ModelForm 기능을 제공하고 있다. 
"""
# class PostForm(forms.Form) :
#     title = forms.CharField(label='제목', max_length=200)
#     content = forms.CharField(label='내용', widget=forms.Textarea)


# ModelForm 상속
class PostForm(ModelForm):
    # Meta 클래스는 반드시 정의해아 함(규칙)
    class Meta:
        # models.py 에 있는 Post
        model = Post
        # 입력받고 싶은 필드
        fields = ['title', 'content']

        # label 을 한국어로 변경
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }

        # span 태그로 input 태그 아래에 도움말 출력
        help_texts = {
            'title': _('제목을 입력해주세요.'),
            'content': _('내용을 입력해주세요.'),
        }

        # 에러 메시지 출력
        error_messages = {
            'name': {
                'max_length': _('제목이 너무 깁니다.')
            }
        }