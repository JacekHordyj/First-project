from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    
    
    class Meta:
        model = User
        fields = ['username','email']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','align':'center','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','align':'center','placeholder':'Username'}),
        }
