from django.db import models


# Create your models here

class abstract(models.Model):
    created_at = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField('修改时间', auto_now=True)  # 修改时间

    class Meta:
        abstract = True

class User_data(abstract):
    name=models.CharField('用户名',max_length=12)
    password=models.CharField('密码',max_length=12)
    tel = models.CharField('电话', max_length=11)
    email= models.CharField('邮箱', max_length=20)

    class Meta:
        db_table = 'user_data'