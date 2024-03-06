from django.shortcuts import render,redirect
from RGUKTApp.models import Student
from .forms import EmForm
from .models import Employee
from django.contrib import messages

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
	b = Employee.objects.all()
	if request.method == "POST":
		n = EmForm(request.POST)
		if n.is_valid():
			n.save()
			messages.success(request,"Record inserted Successfully")
			return redirect('/')
	n = EmForm()
	return render(request,'dy/empy.html',{'z':n,'p':b})

def empup(request,n):
	t = Employee.objects.get(id=n)
	if request.method == "POST":
		m = EmForm(request.POST,instance=t)
		if m.is_valid():
			m.save()
			messages.info(request,"Record Updated Successfully")
			return redirect('/')
	m = EmForm(instance=t)
	return render(request,'dy/emupdt.html',{'v':m})

def empdd(request,q):
	j = Employee.objects.get(id=q)
	if request.method == "POST":
		j.delete()
		messages.warning(request,'Record Deleted Successfully')
		return redirect('/')
	return render(request,'dy/empdt.html',{'s':j})