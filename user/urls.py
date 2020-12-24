from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^login/$', views.login,name='denglu'),
    url(r'^regist/$', views.regist,name='zhuace')
]
