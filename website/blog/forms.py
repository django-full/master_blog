from django import forms
from django.forms import ModelForm

from . import models


class CommentForms(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': "usercomment",
        'placeholder': "Type your comment",
        'rows': '3'
    }))

    class Meta:
        model = models.Comment
        fields = ('content',)
