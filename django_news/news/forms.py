from dataclasses import fields
from pyexpat import model
from statistics import mode
from typing import Text
from .models import Comment, Post, Tag, User
from django import forms
from django.forms import fields, widgets


class CommentForm(forms.Form):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )


class PostCreateForm(forms.ModelForm):
    """Eorm definition for PostCreate"""
    class Meta:
        """Meta definition for PostCreateform."""
        model = Post
        fields = ('title', 'text', "tag_state")


class Tag_Form(forms.ModelForm):
    class Meta:
        fields = ['text']
        model = Tag


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form_controll'}),
            'username': forms.TextInput(attrs={'class': 'form_controll', 'readonly': ''}),
            'first_name': forms.TextInput(attrs={'class': 'form_controll'}),
            'last_name': forms.TextInput(attrs={'class': 'form_controll'}),

        }
