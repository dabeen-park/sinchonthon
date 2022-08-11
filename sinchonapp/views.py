from django.shortcuts import render, redirect
import os
from .models import Person
# Create your views here.


def home(request):
    return render(request, 'index.html')


def mypage(request):
    # 만약 이미 신청서를 작성했다면 입금하세요 페이지로 이동하도록 하기
    # author id만 가져와서 비교....
    blogs = Person.objects.all()
    blog_list = blogs.filter(author_id=request.user.id)
    if blog_list.count() != 0:  # 만약 신청서를 하나라도 냈다면
        blog_team = blog_list[0].team
        if not blog_team:  # 만약 팀칸이 비어있다면,
            return render(request, 'sinchong2.html')
        else:
            return render(request, 'mypage3.html')

    return render(request, 'mypage.html')


def mypage2(request):
    return render(request, 'mypage2.html')


def mypage3(request):
    # 팀결과를 보여준다. 만약 팀칸이 빈칸이면 안보여줌..!
    return render(request, 'mypage3.html')

# 신청 form 을 보여주는 함수


def sinchong(request):
    # 만약 이미 신청서를 작성했다면 입금하세요 페이지로 이동하도록 하기
    # 만약 이미 신청서를 작성했다면 입금하세요 페이지로 이동하도록 하기
    # author id만 가져와서 비교....
    blogs = Person.objects.all()
    blog_list = blogs.filter(author_id=request.user.id)
    if blog_list.count() != 0:  # 만약 신청서를 하나라도 냈다면
        blog_team = blog_list[0].team
        if not blog_team:  # 만약 팀칸이 비어있다면,
            return render(request, 'sinchong2.html')
        else:
            return render(request, 'mypage3.html')

    return render(request, 'mypage.html')

# 신청 form을 저장해주는 함수


def create(request):
    if (request.method == "POST"):
        post = Person()
        post.university = request.POST['university']
        post.name = request.POST['name']
        post.track = request.POST['track']
        post.smallTallk = request.POST['smallTallk']
        current_user = request.user
        post.author = current_user.username
        post.author_id = current_user.id
        post.save()
    return redirect('sinchong2')


def sinchong2(request):
    return render(request, 'sinchong2.html')
