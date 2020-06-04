import os
from django.db import models
from uuid import uuid4
from rentalsystem.settings import MEDIA_ROOT
# Create your models here.

# 图片组表


class PictureGroup(models.Model):
    # 图片组id
    pg_id = models.AutoField(primary_key=True)

    pg_1 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', null=False)
    pg_2 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_3 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_4 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_5 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_6 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_7 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_8 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d', blank=True, null=True)
    pg_9 = models.ImageField(
        upload_to='images/PictureGroup/%Y/%m/%d',  blank=True, null=True)
