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
        if len(ret) == 0:
            return JsonResponse({'success': False, 'exc': 'EMPTY'})
        return JsonResponse({'success': True, 'exc': '', 'data': ret})
    return JsonResponse({'success': True, 'exc': '', 'data': ret})

def picsToPath(pg):
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
        return ret
    return ret

def upload(request):
    if request.method == "POST":
        img_file = request.FILES.getlist("image[]")
        pg = models.PictureGroup()
        try:
            print(len(img_file))
            for i in range(0, len(img_file)):
                f = img_file[i]
                setattr(pg, 'pg_'+str(i+1), img_file[i])
            pg.save()
        except:
            return JsonResponse({'success': False, 'exc': 'UPLOAD_FAIL'})
        return JsonResponse({'success': True, 'exc': '', 'id': pg.pg_id})
    return JsonResponse({'success': False, 'exc': 'POSTONLY'})


def append(request):
    if request.POST:
        img_file = request.FILES.getlist("image")
        try:
            pg = models.PictureGroup.objects.get(pg_id=request.POST['pgid'])
            start = request.POST['start']
        except:
            return JsonResponse({'success': False, 'exc': 'GROUP_404', })
        try:
            for i in range(len(img_file)):
                f = img_file[i+start]
                setattr(pg, 'pg_'+str(i+start), img_file[i+start])
            pg.save()
        except:
            return JsonResponse({'success': False, 'exc': 'APPEND_FAIL'})
        return JsonResponse({'success': True, 'exc': '', 'id': pg.pg_id})
    return JsonResponse({'success': False, 'exc': 'POSTONLY'})


def remove(request):
    try:
        pg_data = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
    try:
        group = models.PictureGroup.objects.get(pg_id=pg_data['pgid'])
        pos = pg_data['id']
        ln = pg_data['len']
    except:
        return JsonResponse({'success': False, 'exc': 'GROUP_404', })
    try:
        setattr(group, 'pg_'+str(pos), None)
        for i in range(pos, ln-1):
            setattr(group, 'pg_' + str(i), getattr(pg, 'pg_' + str(i + 1)))
        setattr(group, 'pg_'+str(ln), None)
        group.save()
    except:
        return JsonResponse({'success': False, 'exc': 'APPEND_FAIL'})
    return JsonResponse({'success': True, 'exc': '', 'id': group.pg_id})
    

def delete(request):
    try:
        pg_data = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
    try:
        group = models.PictureGroup.objects.get(pg_id=pg_data['pgid'])
        group.delete()
    except:
        return JsonResponse({'success': False, 'exc': 'GROUP_404', })
