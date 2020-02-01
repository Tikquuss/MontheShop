from django import forms
from .models import Demandeur

class SignInForm(forms.ModelForm):
    class Meta:
        model = Demandeur
        fields = ('username', 'password')
    

class LoginForm(forms.ModelForm):
    class Meta:
        model = Demandeur
        fields = ('username', 'password')
    

