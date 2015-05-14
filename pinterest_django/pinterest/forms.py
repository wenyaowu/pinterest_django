__author__ = 'evanwu'
from django import forms

from models import Pin, Board, Category


class PinForm(forms.ModelForm):

    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def __init__(self, user, *args, **kwargs):  # Include user variable so we can pass it to form in view.
        super(PinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)

    class Meta:
        model = Pin
        exclude = ('likes', )


class BoardForm(forms.ModelForm):

    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Board
        exclude = ('user', 'slug', )


class PinPinForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(PinPinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)

    class Meta:
        model = Pin
        fields = ('board', )
