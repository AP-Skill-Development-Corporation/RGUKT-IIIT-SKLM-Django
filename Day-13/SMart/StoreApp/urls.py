from django.urls import path
from StoreApp import views
from django.contrib.auth import views as vd

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('reg/',views.register,name="rg"),
	path('login/',vd.LoginView.as_view(template_name="login.html"),name="lg"),
	path('logout/',vd.LogoutView.as_view(template_name="logout.html"),name="lgo"),
]