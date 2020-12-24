import re

from django import forms
from user.models import User_data

class RegistForm(forms.Form):
    username=forms.CharField(label='用户名称',max_length=12)
    password=forms.CharField(label='输入密码',max_length=24,widget=forms.PasswordInput)
    password_verify= forms.CharField(label='确认密码', max_length=24,widget=forms.PasswordInput)
    tel= forms.CharField(label='联系方式', max_length=11,help_text='（输入手机号码）')
    email=forms.EmailField(label='电子邮箱',max_length=24,help_text='（用于找回密码）')
    # remark=forms.CharField(label='备注信息',max_length=256,widget=forms.FileInput)
    # age=forms.IntegerField(label='年龄',widget=forms.NumberInput)

    def clean_tel(self):
        tel=self.cleaned_data['tel']
        print(tel)
        #判断用户名是否为手机号码
        pattern='^0{0,1}1[0-9]{10}$'
        if not re.search(pattern,tel):
            raise forms.ValidationError('请输入正确的手机号码')
        else:
            return tel

    def clean(self):
        clean_data = super().clean()
        print(clean_data)
        username = clean_data.get('username', None)
        if username:
            # 查询用户名和密码匹配的用户
            count = User_data.objects.filter(name=username).count()
            if count !=0:
                raise forms.ValidationError('用户名已被使用')
            else:
                print('存在这个用户')
                return clean_data



class LoginForm(forms.Form):
    username=forms.CharField(label='用户名称',max_length=12)
    password=forms.CharField(label='用户密码',max_length=24,widget=forms.PasswordInput)

    def clean(self):
        clean_data = super().clean()
        print(clean_data)
        username = clean_data.get('username', None)
        password = clean_data.get('password', None)
        if username and password:
            # 查询用户名和密码匹配的用户
            count = User_data.objects.filter(name=username, password=password).count()
            if count == 0:
                raise forms.ValidationError('用户名和密码不匹配')
            else:
                print('存在这个用户')
                return clean_data