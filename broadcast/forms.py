from django import forms
from .models import BTopic, BEntry

class BTopicForm(forms.ModelForm):
    class Meta:
        model= BTopic
        fields= ['text']
        labels={'text':'Broadcast Topic'}

class BEntryForm(forms.ModelForm):
    class Meta:
        model = BEntry
        fields = ['text']
        labels={'text':'Broadcast Entry'}
        widgets= {'text': forms.Textarea(attrs={'cols':90})}
