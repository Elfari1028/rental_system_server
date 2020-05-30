from django.db import models

# Create your models here.
from rentalsystem.settings import MEDIA_ROOT


# 用户表
class User(models.Model):
    # 用户id
    u_id = models.AutoField(primary_key=True)

    # 用户昵称
    u_name = models.CharField(max_length=20, null=False)

    # 用户密码
    u_passwd = models.CharField(max_length=128, null=False)

    # 用户头像
    u_avatar = models.ImageField(
        upload_to='images/User/%Y/%m/%d', null=False, max_length=100)

    # 用户类型
    u_type = models.IntegerField(null=False)

    # 用户电话
    u_tel = models.CharField(max_length=20, null=False)

    # 用户邮箱
    u_email = models.CharField(max_length=50, blank=True, null=False)

    # 用户简介
    u_intro = models.CharField(max_length=256, null=True)

    # 用户性别
    u_sex = models.IntegerField(null=False)

    # 用户年龄
    u_age = models.IntegerField(null=False)

    c_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
