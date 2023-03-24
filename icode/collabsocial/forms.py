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
        'placeholder': 'Add the Stacks...'
        })
    )
    

    class Meta:
        model = Post
        fields = ['body', 'stacks']