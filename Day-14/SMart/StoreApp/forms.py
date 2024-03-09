# from django.contrib.auth.models import User
from StoreApp.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Email Id",
			}),
		}

class UpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","sage","simg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"sage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			}),
		}