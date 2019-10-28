from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Ad',max_length=30,required=False, help_text='')
    last_name = forms.CharField(label='Soyad',max_length=30, required=False, help_text='')
    email = forms.EmailField(label='Email',max_length=254, help_text='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1' )

    def __init__(self, *args, **kwargs):
            # first call parent's constructor
            super(SignUpForm, self).__init__(*args, **kwargs)
            # there's a `fields` property now
            self.fields['username'].required = False
            self.fields['username'].label = 'Username'
            self.fields['username'].help_text = ' '
            self.fields['first_name'].required = False
            self.fields['email'].required = False
            self.fields['last_name'].required = False
            self.fields['password1'].required = False
            # self.fields['email'].help_text = ''
            self.fields['password1'].help_text = ''
            self.fields['password1'].label = 'Şifrə'
            del self.fields['password2']

           