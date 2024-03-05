from .models import Employee
from django import forms

class EmForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["epid","ename","edesg","esal"]
		widgets = {
		"epid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Emp Id",
			}),
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Name",
			}),
		"edesg":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"esal":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Salary",
			"max":"25000",
			"min":"12000",
			}),
		}