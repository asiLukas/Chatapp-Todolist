from django import forms
from .models import ToDoList
from django.utils import timezone
import django.utils.timezone


class ToDoForm(forms.ModelForm):
    item = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your task'
    }))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Any comments(not required)',
        'rows': 5

    }))
    deadline = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Not required'

    }))


    class Meta:
        model = ToDoList
        fields = ['item', 'comments', 'created', 'deadline']


'''class INTODOForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['todo', 'deadline', 'complete']'''
