from django import forms
from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['url','name']
        #help_texts={'name':'enter only alphabets'}
        widgets={'name':forms.PasswordInput}






