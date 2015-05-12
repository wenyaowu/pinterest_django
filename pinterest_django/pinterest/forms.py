__author__ = 'evanwu'
from django import forms

from models import Pin, Board, Category


class PinForm(forms.ModelForm):

    title = forms.CharField(max_length=256, help_text='Title: ')
    description = forms.CharField(max_length=1024, help_text='Description: ')
    image = forms.ImageField(help_text='Upload image: ')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text='Choose a category: ')
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def __init__(self, user, *args, **kwargs):  # Include user variable so we can pass it to form in view.
        super(PinForm, self).__init__(*args, **kwargs)
        self.board = forms.ModelChoiceField(queryset=Board.objects.filter(user=user))

    class Meta:
        model = Pin
        exclude = ('likes', )
