from django import forms
from .models import Page    #사용할 모델 가져오기

class PageForm(forms.ModelForm):

    class Meta:
        model = Page    #모델 폼에서 사용할 모델과 필드 명시
        fields = ['title', 'content', 'feeling', 'score', 'dt_created']
