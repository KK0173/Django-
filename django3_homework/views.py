import json
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import auth
from django.contrib.auth import authenticate, login

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 生payload部分的方法
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 生成jwt的方法

#  {'exp': xxx, 'email': '', 'user_id': 1, 'username': 'admin'}
# user：登录的用户对象
# payload = jwt_payload_handler(user)   # 生成payload, 得到字典
# token = jwt_encode_handler(payload)   # 生成jwt字符串

# def index(request):
# #     context={
# #         'hello':'hello world'
# #     }
# #     return render(request,'index.html',context)
#     print('收到请求')
#     return JsonResponse({'request': 'get请求'})
#
#
from django.urls import reverse

from user.models import User, Post


def login(request):
    if request.method == 'GET':
        return render(request, 'front/login.html')
        # print('it is get request')
        # form = request.GET.get('username')
        # print(form)
        # return JsonResponse({'request': 'get请求'})
    else:  # 从这里开始接受post请求
        json_result = json.loads(request.body)
        if json_result['to'] == 'regist':
            list = User.objects.filter(name=json_result['name'])
            if len(list) == 0:
                user = User(name=json_result['name'], password=json_result['password'])  # 新建数据条目
                user.save()  # 保存数据
                return JsonResponse({'request': '注册请求', "注册结果": "注册成功"})
            elif len(list) == 1:
                return JsonResponse({'request': '注册请求', "注册结果": "注册失败，该用户名已经存在"})
        elif json_result['to'] == 'login':  # 登陆请求
            list = User.objects.filter(name=json_result['name'], password=json_result['password'])
            if len(list) == 1:
                random_string = str(uuid.uuid4())
                # username = json_result['name']
                # password = json_result['password']
                # user_obj = auth.authenticate(username=username, password=password)
                # print(user_obj.username)
                # if user_obj is not None:
                #     auth.login(request, user_obj)
                #     print('用户已经登陆')
                # request.session['user_id']=json_result['name']
                # return redirect('http://127.0.0.1:8000/index/')  //这里不能使用跳转页面
                # request.session['LOGIN_SESSION_ID']=json_result['name'] #尝试用session的方法但是前后端分离的话就失效了
                # user=User.objects.filter(name=json_result['name'])
                # payload = jwt_payload_handler(user)
                # token = jwt_encode_handler(payload)  #这里生成了jwt
                # return redirect(reverse('index'))
                # print(request.session['LOGIN_SESSION_ID'])
                random_string = str(uuid.uuid4())
                user_obj = User.objects.get(name=json_result['name'])
                user_obj.token = random_string
                user_obj.save()
                print(user_obj.token)
                return JsonResponse({'request': '登陆请求', "登陆结果": "登陆成功", 'token': random_string})
            else:
                return JsonResponse({'request': '登陆请求', "登陆结果": "登陆失败，用户名与密码不匹配"})


def index(request):
    if request.method == 'POST':
        json_result = json.loads(request.body)
        list = Post.objects.all()
        user_obj = User.objects.get(token=json_result['token'])
        if not user_obj:
            print('还没登陆')
            return
        else:
            print(user_obj.name)
            show_name = '欢迎您，用户' + user_obj.name
            return JsonResponse({'name': show_name, "post_number": len(list)})
        # user_id=request.session['user_id']
        # print('it is get request')
        # if request.user.is_authenticated():
        #     print('用户已经登陆')
    # else:
    #     list = Post.objects.all()
    #     return JsonResponse({'name': request.session['LOGIN_SESSION_ID'], "post_number": len(list)})

import datetime
now_time = datetime.datetime.now().strftime('%Y-%m-%d')

def add_post(request):
    print('收到请求')
    json_result = json.loads(request.body)
    print(json_result)
    if json_result['time']=='':
        json_result['time']=now_time
    if json_result['address']=='':
        json_result['address']='上海交通大学'
    p = Post(time=json_result['time'], address=json_result['address'], discription=json_result['discription'])
    p.save()
    print("保存成功")
    return JsonResponse({"发布结果": "发布成功！！"})

def get_list(request):
    list_obj=Post.objects.all()
    list=[]
    for i in list_obj:
        a={
            'time':i.time,
            'address':i.address,
            "discription":i.discription,
        }
        list.append(a)
    str(list)
    print(list)
    return JsonResponse({"list": list})
