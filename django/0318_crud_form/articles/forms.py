from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='title',
    )
    content = forms.CharField(
        label='content',
        widget=forms.Textarea(
            'cols': 30,
            'rows': 5,
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
