from django.shortcuts import HttpResponse, redirect, reverse, render
from django.http.response import JsonResponse

import random
import simplejson
import hashlib
import re

from . import json_package
from . import models
# Create your views here.


def obtainPics(request):
    try:
        pg_data = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
    try:
        pg = models.PictureGroup.objects.get(pg_id=pg_data['id'])
    except:
        return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
    ret = []
    try:
        ret.append(pg.pg_1.url)
        ret.append(pg.pg_2.url)
        ret.append(pg.pg_3.url)
        ret.append(pg.pg_4.url)
        ret.append(pg.pg_5.url)
        ret.append(pg.pg_6.url)
        ret.append(pg.pg_7.url)
        ret.append(pg.pg_8.url)
        ret.append(pg.pg_9.url)
    except:
        if len(ret) == 0: return JsonResponse({'success': False, 'exc': 'EMPTY'})
        return JsonResponse({'success': True, 'exc': '', 'data': ret})
    return JsonResponse({'success': True, 'exc': '', 'data': ret})


def upload(request):
    if request.POST:
        img_file = request.FILES.getlist("image")
        pg = models.PictureGroup()
        try:
            for i in range(len(img_file)):
                f = img_file[i]
                setattr(pg, 'pg_'+str(i), img_file[i])
            pg.save()
        except: return JsonResponse({'success':False, 'exc':'UPLOAD_FAIL'})
        return JsonResponse({'success': True, 'exc': '','data':pg.pg_id})
    return JsonResponse({'success': False, 'exc': 'POSTONLY'})
