from django.shortcuts import HttpResponse, redirect, reverse, render
from django.http.response import JsonResponse
from django.core.mail import send_mail

import random
import simplejson
import hashlib
import re
import sys

from . import json_package
from . import models
from house.models import House, RentalOrder
from picgroup.models import PictureGroup
from picgroup.views import picsToPath
from account.models import User
from house.views import houseAsJson, orderToJson
from account.views import userToJson
# POST send request


def getallRqs(request):
    if(request.method == 'GET'):
        try:
            rqs = models.SupportRequest.objects.all()
        except:
            return JsonResponse({'success': False, 'exc': 'GET ALL FAIL'})
        ret = []
        try:
            for rq in rqs:
                ret.append(supportRequestToJson(rq))
        except:
            return JsonResponse({'success': False, 'exc': 'ADD ALL FAIL'})
        return JsonResponse({'success': True, 'data': ret})


def createRequest(request):
    try:
        requestdata = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        pg = PictureGroup.objects.get(pg_id=requestdata['pgid'])
    except:
        return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
    try:
        user = User.objects.get(u_id=requestdata['uid'])
    except:
        return JsonResponse({'success': False, 'exc': 'USER_ID_404', })
    try:
        newRequest = models.SupportRequest()
        newRequest.u_id = user
        newRequest.sr_type = requestdata['type']
        newRequest.sr_status = requestdata['status']
        newRequest.sr_content = requestdata['content']
        newRequest.ro_id = RentalOrder.objects.get(ro_id=requestdata['order'])
        newRequest.pg_id = pg
        newRequest.save()
    except:
        return JsonResponse({'success': False, 'exc': 'H_CREATE_FAIL', })
    return JsonResponse({'success': True, 'exc': ''})


def changeRqStatus(request):
    try:
        requestdata = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        rq = models.SupportRequest.objects.get(sr_id=requestdata['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
    rq.sr_status = requestdata['status']
    rq.save()
    return JsonResponse({'success': True, 'exc': ''})


def replyToRequest(request):
    try:
        requestdata = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    reply = models.SupportRequestConversation()
    if(requestdata["pgid"] != -1):
        try:
            pg = PictureGroup.objects.get(pg_id=requestdata['pgid'])
            reply.pg_id = pg
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
    try:
        sr = models.SupportRequest.objects.get(sr_id=requestdata['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'SR_ID_404', })
    try:
        user = User.objects.get(u_id=request.session['user_id'])
    except:
        return JsonResponse({'success': False, 'exc': 'QR_ID_404', })

    try:
        reply.sr_id = sr
        reply.u_id = user
        reply.src_content = requestdata['content']
        reply.save()
    except:
        return JsonResponse({'success': False, 'exc': 'SR_ID_404', })
    return JsonResponse({'success': True, 'exc': '', 'data': replyToJson(reply)})


def replyToJson(reply):
    pgid = None
    imagePaths = None
    try:
        picgroup = reply.pg_id
        pgid = picgroup.pg_id
        imagePaths = picsToPath(picgroup)
    except:
        picgroup = None
    return {
        'id': reply.src_id,
        'content': reply.src_content,
        'pgid': pgid,
        'images': imagePaths,
        'user': userToJson(reply.u_id),
        'time': reply.src_time,
        'srid': reply.sr_id.sr_id
    }


def supportRequestToJson(support):
    rentee = None
    service = None
    maintenance = None
    order = None
    pg = None
    try:
        order = support.ro_id
        rentee = support.u_id
        service = support.res_u_id
        maintenance = support.fix_u_id
        pg = support.pg_id
    except:
        print(sys.exc_info())
    return {
        'id': support.sr_id,
        'status': support.sr_status,
        'type': support.sr_type,
        'content': support.sr_content,
        'create': support.sr_time,
        'order': orderToJson(order),
        'pgid': pg.pg_id,
        'images': picsToPath(pg),
        'rentee': userToJson(rentee),
        'maintenance': userToJson(maintenance),
        'respondant': userToJson(service),
    }


def getConverstation(request):
    try:
        data = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        sr = models.SupportRequest.objects.get(sr_id=data['id'])
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        replies = models.SupportRequestConversation.objects.filter(
            sr_id=data['id'])
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    jsonreplies = []
    for element in replies:
        jsonreplies.append(replyToJson(element))
    return JsonResponse({'success': True, 'data': jsonreplies})


def rate(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        try:
            ratings = models.SupportRequestRating()
            rq = models.SupportRequest.objects.get(sr_id=data['srid'])
            ratings.sr_id = rq
            rq.sr_status =  5
            ratings.srr_stars = data['stars']
            ratings.srr_content = data['content']
            rq.save()
            ratings.save()
        except:
            JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        return JsonResponse({'success':True})
    return JsonResponse({'success':False,'exc':'bad method'})

def getRateFor(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        rt = None
        try:
            rq = models.SupportRequest.objects.get(sr_id=data['srid'])
            if(rq.sr_status != 5):
                return JsonResponse({'success': False, 'exc': 'NOT CLOSED YET', })
            rt = models.SupportRequestRating.objects.get(sr_id=rq)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        return JsonResponse({'success':True,'data':ratingsToJson(rt)})
    return JsonResponse({'success':False,'exc':'bad method'})

def ratingsToJson(rt):
    if(rt == None):
        return None
    return {
        "srid": rt.sr_id.sr_id,
        "stars":rt.srr_stars,
        "content":rt.srr_content,
    }

def closeRq(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        try:
            rq = models.SupportRequest.objects.get(sr_id=data['srid'])
            rq.sr_status =  4
            rq.save()
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        return JsonResponse({'success':True})
    return JsonResponse({'success':False,'exc':'bad method'})

def appointRes(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        try:
            rq = models.SupportRequest.objects.get(sr_id=data['srid'])
            res = User.objects.get(u_id=data['fid'])
            if(res.u_type != 3):
                return JsonResponse({'success': False, 'exc': 'WRONG ACCOUNT PRIV', })
            rq.sr_status =  2
            rq.res_u_id = res
            rq.save()
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        return JsonResponse({'success':True})
    return JsonResponse({'success':False,'exc':'bad method'})

def appointFix(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        try:
            rq = models.SupportRequest.objects.get(sr_id=data['srid'])
            res = User.objects.get(u_id=data['fid'])
            if(res.u_type != 2):
                return JsonResponse({'success': False, 'exc': 'WRONG ACCOUNT PRIV', })
            rq.sr_status =  3
            rq.res_u_id = res
            rq.save()
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        return JsonResponse({'success':True,'data':userToJson(res)})
    return JsonResponse({'success':False,'exc':'bad method'})