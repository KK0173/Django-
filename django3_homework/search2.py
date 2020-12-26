from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
from user.models import User


# def search_post(request):
#     ctx = {}  #接受容器
#     if request.POST:
#         ctx['rlt'] = request.POST['q']
#         user1=Test(name=request.POST['q'])
#         user1.save()
#     return render(request, "post.html", ctx)