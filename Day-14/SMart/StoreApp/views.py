from django.shortcuts import render,redirect
from .forms import RegForm,UpForm
from django.core.mail import send_mail
from SMart import settings
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'ht/home.html')

def about(request):
	return render(request,'about.html')

def register(request):
	if request.method == "POST":
		p = RegForm(request.POST)
		if p.is_valid():
			v = p.save(commit=False)
			s = send_mail("S-Mart Registration","Thanks for Subscribing to this site",settings.EMAIL_HOST_USER,[v.email]) 
			if s == 1:
				v.save()
				messages.success(request,"Registered Successfully please check your mail for confirmation")
				return redirect('/login/')
			else:
				messages.warning(request,"Not registered please enter Your correct mailid")
				return redirect('/reg/')
	else:
		p = RegForm()
	return render(request,'register.html',{'z':p})

def profile(request):
	return render(request,"ht/profile.html")

def upfle(request):
	if request.method == "POST":
		k = UpForm(request.POST,request.FILES,instance=request.user)
		if k.is_valid():
			k.save()
			messages.success(request,"Profile Updated Successfully")
			return redirect('/pfle')
	k = UpForm(instance=request.user)
	return render(request,'ht/updpfle.html',{'m':k})