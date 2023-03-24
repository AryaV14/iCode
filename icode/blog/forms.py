from django import forms
from .models import Blog


    
class BlogForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows' : '5',
        'placeholder': 'Erite something..'
        })
    )
   

    class Meta:
        model = Blog
        fields = ['body']