from django.shortcuts import render,redirect
from RGUKTApp.models import Student
from .forms import EmForm
# Create your views here.

def std(request):
	p = Student.objects.all()
	if request.method == "POST":
		a = Student(stid=request.POST['d'],sname=request.POST['n'],sbranch=request.POST['b'],syear=request.POST['y'])
		a.save()
		return redirect('/st/')
	return render(request,'dy/stdnt.html',{'data':p})

def stpd(request,g):
	k = Student.objects.get(id=g)
	if request.method == "POST":
		k.stid = request.POST['sd']
		k.sname = request.POST['sn']
		k.sbranch = request.POST['sb']
		k.syear = request.POST['sy']
		k.save()
		return redirect('/st/')
	return render(request,'dy/stupdate.html',{'dc':k})

def stdd(request,a):
	c = Student.objects.get(id=a)
	if request.method == "POST":
		c.delete()
		return redirect('/st/')
	return render(request,'dy/stdlt.html',{'h':c})

def emp(request):
	n = EmForm()
	return render(request,'dy/empy.html',{'z':n})