from django.db import models

# Create your models here.
from rentalsystem.settings import MEDIA_ROOT


# 用户表
class Users(models.Model):
    # 用户id
    u_id = models.AutoField(primary_key=True)

    # 用户昵称
    u_name = models.CharField(max_length=20, null=False)

    # 用户密码
    u_passwd = models.CharField(max_length=20, null=False)

    # 用户头像
    u_avatar = models.ImageField(upload_to='images/Users/%Y/%m/%d', null=False, max_length=100)

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


# 房源表
class House(models.Model):
    # 房屋id
    h_id = models.AutoField(primary_key=True)

    # 房屋标题
    h_name = models.CharField(max_length=50, null=False)

    # 房屋状态
    h_status = models.IntegerField(null=False)

    # 房屋类型
    h_type = models.IntegerField(null=False)

    # 房屋介绍
    h_intro = models.CharField(max_length=256, null=False)

    # 单位时间价格
    h_price = models.IntegerField(null=False)

    # 地点信息
    h_location = models.CharField(max_length=256, null=False)

    # 图片组id
    pg_id = models.ForeignKey('PictureGroup', on_delete=models.CASCADE, null=False)


# 订单表
class RentalOrder(models.Model):
    # 工单id
    ro_id = models.AutoField(primary_key=True)

    # 工单状态
    ro_status = models.IntegerField(null=False)

    # 工单类型
    ro_type = models.IntegerField(null=False)

    # 订单金额
    ro_amount = models.IntegerField(null=False)

    # 创建时间(自动生成，只读)
    ro_time = models.DateTimeField(auto_now_add=True, null=False)

    # 租期开始时间
    ro_start = models.DateTimeField(null=False)

    # 租期结束时间
    ro_end = models.DateTimeField(null=False)

    # 租客和审核客服id需要定义related_name，否则冲突
    # 租客id（外键）
    u_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=False, related_name='ro_u_id')

    # 房屋id（外键）
    h_id = models.ForeignKey('House', on_delete=models.CASCADE, null=False)

    # 审核客服（外键）
    res_u_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True, related_name='ro_res_u_id')


# 工单表
class SupportRequest(models.Model):
    # 工单id
    sr_id = models.AutoField(primary_key=True)

    # 工单状态
    sr_status = models.IntegerField(null=False)

    # 工单类型
    sr_type = models.IntegerField(null=False)

    # 工单内容
    sr_type = models.CharField(max_length=256, null=False)

    # 创建时间（自动生成，只读）
    sr_time = models.DateTimeField(auto_now_add=True, null=False)

    # 租客id,审核客服id,维修工id需要定义related_name，否则冲突
    # 租客id（外键）
    u_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=False, related_name='sr_u_id')

    # 图片组id（外键）
    pg_id = models.ForeignKey('PictureGroup', on_delete=models.CASCADE, null=True)

    # 负责客服id（外键）
    res_u_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True, related_name='sr_res_u_id')

    # 接入维修工（外键）
    fix_u_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True, related_name='sr_fix_u_id')


# 工单回复表
class SupportRequestConversation(models.Model):
    # 回复id
    src_id = models.AutoField(primary_key=True)

    # 回复内容
    src_content = models.CharField(max_length=256, null=False)

    # 回复时间（自动生成，只读）
    src_time = models.DateTimeField(auto_now_add=True, null=False)

    # 所属工单id（外键）
    sr_id = models.ForeignKey('SupportRequest', on_delete=models.CASCADE, null=False, )

    # 用户id（外键）
    u_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=False)

    # 图片组id（外键）
    pg_id = models.ForeignKey('PictureGroup', on_delete=models.CASCADE, null=False)


# 工单评价表
class SupportRequestRating(models.Model):
    # 工单评价id
    srr_id = models.AutoField(primary_key=True)

    # 工单评价内容
    srr_content = models.CharField(max_length=256, null=False)

    # 工单评价星级
    srr_stars = models.IntegerField(null=False)

    # 所属工单（外键）
    sr_id = models.ForeignKey('SupportRequest', on_delete=models.CASCADE, null=False)


# 图片组表
class PictureGroup(models.Model):
    # 图片组id
    pg_id = models.AutoField(primary_key=True)

    pg_1 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', null=False)
    pg_2 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_3 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_4 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_5 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_6 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_7 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_8 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_9 = models.ImageField(upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
