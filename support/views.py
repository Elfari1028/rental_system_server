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
from house.models import House,RentalOrder
from picgroup.models import PictureGroup
from picgroup.views import picsToPath
from account.models import User
from house.views import houseAsJson,orderToJson
from account.views import userToJson
# POST send request
def createRequest(request):
    try: 
        requestdata= simplejson.loads(request.body)
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
    return JsonResponse({'success':True,'exc':''})

def changeRqStatus(request):
    try: 
        requestdata= simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        rq = models.SupportRequest.objects.get(sr_id=requestdata['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
    rq.sr_status = requestdata['status']
    rq.save()
    return JsonResponse({'success':True,'exc':''})


def replyToRequest(request):
    try:
        requestdata = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    reply = models.SupportRequestConversation()
    if(requestdata["pgid"] != -1):
        try:
            pg = PictureGroup.objects.get(pg_id=requestdata['pgid'])
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
    try:
        sr = models.SupportRequest.objects.get(sr_id=requestdata['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'SR_ID_404', })
    try:
        user = models.SupportRequest.objects.get(sr_id=requestdata['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'SR_ID_404', })
    
    try:
        reply.pg_id = pg
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
        picgroup = PictureGroup.objects.get(pg_id=reply.pg_id)
        pgid = picgroup.pg_id
        imagePaths = picsToPath(picgroup)
    except:
        picgroup = None
    return {
        'id':reply.sr_id,
        'content':reply.sr_content,
        'pgid': pgid,
        'imagePaths' : imagePaths,
        'uid':reply.u_id,
        'time':reply.src_time,
        'srid': reply.sr_id
    }

def supportRequestToJson(support):
    rentee = None
    service = None
    maintenance = None
    order = None
    try:
        order = support.ro_id
        rentee = support.u_id
        service = support.res_u_id
        maintenance = support.fix_u_id
    except:
        print(sys.exc_info()) 
    return {
        'id':support.sr_id,
        'status': support.sr_status,
        'type':support.sr_type,
        'content':support.sr_content,
        'create': supportRequestToJson.create,
        'order': orderToJson(order),
        'rentee': userToJson(rentee),
        'maintenance': userToJson(maintenance),
        'respondant':userToJson(service),
    }



def getConverstation(request):
    try: 
        data = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        sr = models.SupportRequest.objects.get(sr_id=data['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        replies = models.SupportRequest.objects.filter(sr_id=data['srid'])
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    jsonreplies = []
    for element in replies:
        jsonreplies.append(replyToJson(element))
    