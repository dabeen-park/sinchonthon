from django.shortcuts import render, redirect
import os
from .models import Person
# Create your views here.
def home(request):
    return render(request, 'index.html')


def mypage(request):
    return render(request, 'mypage.html')

def mypage2(request):
    return render(request, 'mypage2.html')

def mypage3(request):
    return render(request, 'mypage3.html')

# 신청 form 을 보여주는 함수
def sinchong(request):
    return render(request, 'sinchong.html')

# 신청 form을 저장해주는 함수
def create(request):
    if (request.method == "POST"):
        post = Person()
        post.university = request.POST['university']
        post.name = request.POST['name']
        post.track =request.POST['track']
        post.smallTallk = request.POST['smallTallk']
        post.save()
    return redirect('sinchong2')


def sinchong2(request):
    return render(request, 'sinchong2.html')

