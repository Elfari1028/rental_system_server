from django.db import models

# 房源表


class House(models.Model):
    # 房屋id
    h_id = models.AutoField(primary_key=True)

    # 房屋标题
    h_name = models.CharField(max_length=50, null=False)

    # 房屋状态
    h_status = models.IntegerField(null=False)

    # 房屋类型
    h_term = models.IntegerField(null=False)

    # 房屋人数
    h_cap = models.IntegerField(null=False)

    # 房屋介绍
    h_intro = models.CharField(max_length=256, null=False)

    # 单位时间价格
    h_price = models.IntegerField(null=False)

    # 地点信息
    h_location = models.CharField(max_length=256, null=False)

    # 图片组id
    pg_id = models.ForeignKey(
        'PictureGroup', on_delete=models.CASCADE, null=False)


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
    u_id = models.ForeignKey(
        'Users', on_delete=models.CASCADE, null=False, related_name='ro_u_id')

    # 房屋id（外键）
    h_id = models.ForeignKey('House', on_delete=models.CASCADE, null=False)

    # 审核客服（外键）
    res_u_id = models.ForeignKey(
        'Users', on_delete=models.CASCADE, null=True, related_name='ro_res_u_id')
