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
from picgroup.models import PictureGroup
from picgroup.views import picsToPath
from account.models import User
from account.views import userToJson
# Create your views here.


def create(request):
    if (request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        try:
            pg = PictureGroup.objects.get(pg_id=data['pgid'])
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
        try:
            house = models.House()
            house.h_title = data['title']
            house.h_cap = data['cap']
            house.h_term = data['term']
            house.h_status = data['status']
            house.h_intro = data['intro']
            house.pg_id = pg
            house.h_location = data['location']
            house.h_price = data['price']
            house.save()
        except:
            return JsonResponse({'success': False, 'exc': 'H_CREATE_FAIL', })
        return JsonResponse({'success': True, 'exc': '','data':houseAsJson(house)})

def getAvailHouses(request):
    if (request.method == 'GET'):
        try:
            houses = models.House.objects.filter(h_status=1)
        except:
            return JsonResponse({'success': False, 'exc': 'GET_ALL_FAIL', })
        ret = []
        try:
            for house in houses:
                ret.append(houseAsJson(house))
        except:
            print(sys.exc_info())
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        return JsonResponse({'success': True, 'data': ret})


def getAllHouses(request):
    if (request.method == 'GET'):
        try:
            houses = models.House.objects.all()
        except:
            return JsonResponse({'success': False, 'exc': 'GET_ALL_FAIL', })
        ret = []
        try:
            for house in houses:
                ret.append(houseAsJson(house))
        except:
            print(sys.exc_info())
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        return JsonResponse({'success': True, 'data': ret})


def houseAsJson(house):
    picgroup = house.pg_id
    paths = picsToPath(picgroup)
    return {
        'id': house.h_id,
        'title': house.h_name,
        'cap': house.h_cap,
        'term': house.h_term,
        'status': house.h_status,
        'intro': house.h_intro,
        'location': house.h_location,
        'price': house.h_price,
        'pgid': picgroup.pg_id,
        'images': paths,
    }


def recommend(request):
    if (request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        ret = []
        try:
            for i in range(data['count']):
                ret.append(houseAsJson(models.House.randoms.random()))
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })

        return JsonResponse({'success': True, 'exc': '', 'data': ret})


def update(request):
    if (request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        try:
            pg = PictureGroup.objects.get(pg_id=data['pgid'])
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
        try:
            house = models.House.objects.get(h_id=data['id'])
            house.h_title = data['title']
            house.h_cap = data['cap']
            house.h_term = data['term']
            house.h_status = data['status']
            house.h_intro = data['intro']
            house.h_location = data['location']
            house.h_price = data['price']
            house.save()
        except:
            return JsonResponse({'success': False, 'exc': 'H_CREATE_FAIL', })
        return JsonResponse({'success': True, 'exc': '', })
def createOrder(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ORDER_OBT_BAD_FORMAT', })
        try:
            newOrder = models.RentalOrder()
            newOrder.ro_amount = data['amount']
            newOrder.h_id = models.House.objects.get(h_id=data['hid'])
            newOrder.u_id = User.objects.get(u_id=data['uid'])
            newOrder.ro_start = data['start']
            newOrder.ro_end = data['end']
            newOrder.ro_status = data['status']
            newOrder.ro_type = data['type'] 
            newOrder.save()           
        except:
            print(sys.exc_info())
            return JsonResponse({'success': False, 'exc': 'ORDER_CREATE_FAIL', })
        return JsonResponse({'success': True, 'exc': '', })

def getUserOrder(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ORDER_OBT_BAD_FORMAT', })
        try:
            user = User.objects.get(u_id=data['uid']) 
            orders = models.RentalOrder.objects.filter(u_id=user)
            ret = []
            for order in orders:
                ret.append(orderToJson(order))
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
        return JsonResponse({'success': True, 'exc': '', 'data':ret})

def getAllOrder(request):
    if(request.method == 'GET'):
        try:
            orders = models.RentalOrder.objects.all()
            ret = []
            for order in orders:
                ret.append(orderToJson(order))
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
        return JsonResponse({'success': True, 'exc': '', 'data':ret})

def updateOrder(request):
    if(request.method == 'POST'):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ORDER_OBT_BAD_FORMAT', })
        try:
            newOrder = models.RentalOrder.objects.get(ro_id=data['id'])
            newOrder.ro_amount = data['amount']
            newOrder.h_id = models.House.objects.get(h_id=data['hid'])
            newOrder.u_id = User.objects.get(u_id=data['uid'])
            newOrder.ro_start = data['start']
            newOrder.ro_end = data['end']
            newOrder.ro_status = data['status']
            newOrder.ro_type = data['type']
            newOrder.save()           
        except:
            print(data['uid'])
            print(sys.exc_info())
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
        return JsonResponse({'success': True, 'exc': '', })

def orderToJson(order):
    respondant =  None
    try:
        respondant = User.objects.get(order.res_u_id)
    except:
        respondant = None
    return {
        'id':order.ro_id,
        'status':order.ro_status,
        'type': order.ro_type,
        'amount':order.ro_amount,
        'create':order.ro_time,
        'start':order.ro_start,
        'end': order.ro_end,
        'house': houseAsJson(order.h_id),
        'rentee': userToJson(order.u_id),
        'respondant':   respondant,
    }