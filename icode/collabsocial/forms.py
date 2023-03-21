from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows' : '5',
        'placeholder': 'Say about the project...'
        })
    )
    stacks = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows' : '5',
        'placeholder': 'The collaborators you need...'
        })
    )

    class Meta:
        model = Post
        fields = ['body', 'stacks']