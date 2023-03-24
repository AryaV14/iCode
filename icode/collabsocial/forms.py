from django import forms
from .models import Post,Stacks

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.stacks
class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows' : '5',
        'placeholder': 'Say about the project...'
        })
    )
    stacks = forms.ModelChoiceField(
        
    queryset= Stacks.objects.all(), 
     widget = forms.CheckboxSelectMultiple
    
    )

    class Meta:
        model = Post
        fields = ['body', 'stacks']