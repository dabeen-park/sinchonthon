"""sinchonthon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from sinchonapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage2/' , views.mypage2, name='mypage2'),
    path('mypage3/' , views.mypage3, name='mypage3'),

    path('sinchong/' , views.sinchong, name='sinchong'),
    path('create/', views.create , name='create'),

    path('sinchong2/' , views.sinchong2, name='sinchong2'),

    #카카오 소셜 로그인
    path('account/', include('allauth.urls')),

    #로그인
    path('login/', accounts_views.login, name='login'),
    #로그아웃
    path('logout/', accounts_views.logout, name='logout'),
    

    
]
