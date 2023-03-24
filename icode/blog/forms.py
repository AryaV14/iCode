from django import forms
from .models import Blog, Comments


    
class BlogForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows' : '5',
        'placeholder': 'Write something..'
        })
    )
   

    class Meta:
        model = Blog
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows' : '3',
        'placeholder': 'Thoughts?..'
        })
    )
   

    class Meta:
        model = Comments
        fields = ['comment']