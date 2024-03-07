from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'ht/home.html')

def about(request):
	return render(request,'about.html')

def register(request):
	return render(request,'register.html')