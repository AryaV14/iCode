from django import forms
from .models import Post


    
class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'class':'textarea',
        'rows' : '5',
        'cols' : '20',
        'placeholder': 'Write about your project'
        })
    )
    

    class Meta:
        model = Post
        fields = ['body']