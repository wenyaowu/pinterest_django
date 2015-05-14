from crispy_forms.bootstrap import StrictButton
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Fieldset, ButtonHolder, HTML

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
        self.helper = FormHelper()
        self.helper.form_id = 'pin_form'
        self.helper.form_method = 'post'
        self.helper.form_action = '/pinterest/create_pin/'

        self.helper.add_input(Submit('Submit', 'Create Pin',css_class="btn-default"))

    class Meta:
        model = Pin
        exclude = ('likes', )


class BoardForm(forms.ModelForm):

    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'board_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'pinterest/create_board'

        self.helper.add_input(Submit('Submit', 'Create Board'))

    class Meta:
        model = Board
        exclude = ('user', 'slug', )


class PinPinForm(forms.ModelForm):

    def __init__(self, user, pin_id, *args, **kwargs):
        super(PinPinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)
        self.helper = FormHelper()
        self.helper.form_id = 'pin_pin_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'pin_pin/'+pin_id+'/'
        self.helper.layout = Layout(
            Fieldset(
                'Choose the board that you want to pin on',
                'board'
            ),
            ButtonHolder(
                Submit('submit', 'Pin Pin', css_class='btn-default'),
                HTML('<button class="btn btn-default" id="pincancel" data-pinid=pin_id'
                     ' data-dismiss="modal">Cancel</button>')
            )
        )

    class Meta:
        model = Pin
        fields = ('board', )
