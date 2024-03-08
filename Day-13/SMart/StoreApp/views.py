from django.shortcuts import render,redirect
from .forms import RegForm

# Create your views here.

def home(request):
	return render(request,'ht/home.html')

def about(request):
	return render(request,'about.html')

def register(request):
	m = {}
	if request.method == "POST":
		p = RegForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/login/')
	p = RegForm()
	return render(request,'register.html',{'z':p})