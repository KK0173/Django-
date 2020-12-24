from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

from django_HomeworkProject.views import index
from user.forms import LoginForm, RegistForm
from user.models import User_data


def reverse(args):
    pass


def regist(request):
    if request.method == 'POST':
        # 如果是post请求，需要接收参数处理内部逻辑
        form = RegistForm(request.POST)
        # 验证表单数据的合法性
        if form.is_valid():
            # 取数据
            data = form.cleaned_data  # 访问表单验证后的数据
            print(data['username'])
            if data['password'] == data['password_verify']:
                User_data.objects.create(name=data['username'], password=data['password'], tel=data['tel'],
                                         email=data['email'])
            # 其他逻辑
                return render(request,'index.html')
    else:
        # 如果是get请求，展示页面
        form = RegistForm()
        print(form.is_bound)
    return render(request, 'user_regist.html', {
        'form': form
    })


def login(request):
    if request.method == 'POST':
        # 如果是post请求，需要接收参数处理内部逻辑
        form = LoginForm(request.POST)
        # 验证表单数据的合法性
        if form.is_valid():
            # 取数据
            data = form.cleaned_data  # 访问表单验证后的数据
            print(data['username'])
            # if data['password']==data['password_verify']:
            #     User_data.objects.create(name=data['username'],password=data['password'],tel=data['tel'],email=data['email'])
            # 其他逻辑
            return render(request,'index.html')
    else:
        # 如果是get请求，展示页面
        form = LoginForm()
        print(form.is_bound)
    return render(request, 'user_login.html', {
        'form': form
    })
