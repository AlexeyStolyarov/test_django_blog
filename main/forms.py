# -*- coding: utf-8 -*-

from django import forms
'''
data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
'''

class BlogItemCommentForm(forms.Form):
    parent_id = forms.CharField(widget=forms.HiddenInput())
    comment_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    text = forms.CharField(label='Комментарий', max_length=2000, widget=forms.Textarea)
    avatar = forms.ImageField(label='Аватар', widget=forms.ClearableFileInput(), required=False)