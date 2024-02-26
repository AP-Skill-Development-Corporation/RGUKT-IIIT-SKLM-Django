from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
	return HttpResponse("Welcome to APSSDC Programs")

def ht(a):
	return HttpResponse("<h2>Hi welcome!!!</h2>")

def ph(request,k):
	return HttpResponse(f"<h2>Hello user {k}</h2>")

def stdnt(request,ag,sn,ad="VJWD"):
	return HttpResponse(f"<h1>Student Data</h1><h4>Name: {sn}</h4><h4>Age: {ag}</h4><h4>Address: {ad}</h4>")

def sh(request,q,a):
	return HttpResponse(f"<h2>Hi user <span style='color:green'>{q}</span></h2><h2>Age is: <span style='color:red'>{a}</span></h2>")

def wp(request,z):
	return HttpResponse(f"<script>alert('Hi User {z}');</script><h4>Welcome User <span style='color:blue'>{z}</span></h4>")

def zy(request):
	return render(request,'demo.html')

def empy(request,e):
	return render(request,'em.html',{'t':e})

def emp(request,eg,en,ed):
	return render(request,'emt.html',{"ename":en,"eid":ed,"eage":eg})

def stdntre(request):
	return render(request,'streg.html')

