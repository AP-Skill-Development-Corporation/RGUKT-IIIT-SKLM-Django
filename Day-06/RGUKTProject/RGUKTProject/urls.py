"""RGUKTProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RGUKTApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('z/',views.greet),
    path('y/',views.ht),
    path('dv/<str:k>/',views.ph),
    path('st/<str:sn>/<int:ag>/',views.stdnt),
    path('nm/<str:q>/<int:a>/',views.sh),
    path('cb/<str:z>/',views.wp),
    path('kn/',views.zy),
    path('hk/<str:e>/',views.empy),
    path('bt/<str:en>/<str:ed>/<int:eg>/',views.emp),
    path('sty/',views.stdntre),
]
