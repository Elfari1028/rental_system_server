from django.shortcuts import HttpResponse, redirect, reverse, render
from django.http.response import JsonResponse
from django.core.mail import send_mail

import random
import simplejson
import hashlib
import re

from . import json_package
from . import models
from picgroup.models import PictureGroup
from picgroup.views import picsToPath
# Create your views here.


def create(request):
    if (request.method == POST):
        try:
            data = simpleJson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        try:
            pg = PictureGroup.objects.get(pg_id=data['pgid'])
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
        try:
            house = models.House()
            house.h_id = data['id']
            house.h_title = data['title']
            house.h_cap = data['cap']
            house.h_term = data['term']
            house.h_status = data['status']
            house.h_intro = data['intro']
            house.pg_id = data['pgid']
            house.h_location = data['location']
            house.h_price = data['price']
            house.save()
        except:
            return JsonResponse({'success': False, 'exc': 'H_CREATE_FAIL', })
        return JsonResponse({'success': True, 'exc': '', })


def getAllHouses(request):
    if (request.method == GET):
        try:
            houses = models.House.objects.all()
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        ret = []
        try:
            for house in houses:
                ret.append(houseAsJson(house))
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        return JsonResponse({'success': True, 'data': ret})


def houseAsJson(house):
    picgroup = PictureGroup.objects.get(pg_id=house.pg_id)
    paths = picsToPath(picgroup)
    return {
        'd': house.h_id,
        'title': house.h_title,
        'cap': house.h_cap,
        'term': house.h_term,
        'status': house.h_status,
        'intro': house.h_intro,
        'location': house.h_location,
        'price': house.h_price,
        'pgid': house.h_pg_id,
        'images': paths,
    }


def recommend(request):
    if (request.method == POST):
        try:
            data = simpleJson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'PIC_OBT_BAD_FORMAT', })
        ret = []
        try:
            for i in Range(data['count']):
                ret.append(houseAsJson(models.House.randoms.random()))
        except:
            return JsonResponse({'success': False, 'exc': 'PG_ID_404', })

        return JsonResponse({'success': True, 'exc': '', 'data': ret})


def update(request):
    return JsonResponse({'success': False, 'exc': 'PG_ID_404', })
