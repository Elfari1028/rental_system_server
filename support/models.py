from django.db import models


# 工单表
class SupportRequest(models.Model):
    # 工单id
    sr_id = models.AutoField(primary_key=True)

    # 工单状态
    sr_status = models.IntegerField(null=False)

    # 工单类型
    sr_type = models.IntegerField(null=False)

    # 工单内容
    sr_content = models.CharField(max_length=256, null=False)

    # 创建时间（自动生成，只读）
    sr_time = models.DateTimeField(auto_now_add=True, null=False)

    # 租客id,审核客服id,维修工id需要定义related_name，否则冲突
    # 租客id（外键）
    u_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, related_name='sr_u_id')
    
    h_id = models.ForeignKey(
        'House', on_delete=models.CASCADE, null=False, related_name='sr_u_id')

    # 图片组id（外键）
    pg_id = models.ForeignKey(
        'PictureGroup', on_delete=models.CASCADE, null=True)

    # 负责客服id（外键）
    res_u_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, related_name='sr_res_u_id')

    # 接入维修工（外键）
    fix_u_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, related_name='sr_fix_u_id')


# 工单回复表
class SupportRequestConversation(models.Model):
    # 回复id
    src_id = models.AutoField(primary_key=True)

    # 回复内容
    src_content = models.CharField(max_length=256, null=False)

    # 回复时间（自动生成，只读）
    src_time = models.DateTimeField(auto_now_add=True, null=False)

    # 所属工单id（外键）
    sr_id = models.ForeignKey(
        'SupportRequest', on_delete=models.CASCADE, null=False, )

    # 用户id（外键）
    u_id = models.ForeignKey('User', on_delete=models.CASCADE, null=False)

    # 图片组id（外键）
    pg_id = models.ForeignKey(
        'PictureGroup', on_delete=models.CASCADE, null=False)


# 工单评价表
class SupportRequestRating(models.Model):
    # 工单评价id
    srr_id = models.AutoField(primary_key=True)

    # 工单评价内容
    srr_content = models.CharField(max_length=256, null=False)

    # 工单评价星级
    srr_stars = models.IntegerField(null=False)

    # 所属工单（外键）
    sr_id = models.ForeignKey(
        'SupportRequest', on_delete=models.CASCADE, null=False)
