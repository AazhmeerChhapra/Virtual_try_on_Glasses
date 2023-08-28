from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from store.models.FielsToBeSent import FieldsToBeSent

class OtpForm(ModelForm):
    token_number=forms.IntegerField(required=True)
    class Meta:
        model=FieldsToBeSent
        fields=['token_number']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']