from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10
    )
    content = forms.CharField(
        label='내용'
    )
    class Meta:
        model = Article
        fields = '__all__'