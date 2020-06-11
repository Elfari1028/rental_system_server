from django.shortcuts import HttpResponse, redirect, reverse, render
from django.http.response import JsonResponse
from django.core.mail import send_mail

import random
import simplejson
import hashlib
import re

from . import json_package
from . import models


# 数据库存储密码加密函数，如果指定或修改salt需要重新加载数据库
def hash_code(s, salt='CabinNav'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def exist_id_check(u_id=''):
    try:
        models.User.objects.get(u_id=u_id)
        return True
    except:
        return False


def exist_tel_check(u_tel=''):
    try:
        models.User.objects.get(u_tel=u_tel)
        return True
    except:
        return False

# 邮箱有效性检查


def mail_check(mail_address):
    regx = re.compile(
        r'^[_a-z0-9-]+(\.[a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$')
    rst = regx.match(mail_address)
    return bool(rst)


# 登录
def login(request):
    try:
        login_data = simplejson.loads(request.body)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    try:
        user = models.User.objects.get(u_tel=login_data['id'])
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_404', })
    if user.u_passwd == hash_code(login_data['password']):
        request.session['is_login'] = True
        request.session['user_id'] = user.u_id
        return JsonResponse({'success': True, 'exc': '', 'data': userToJson(user), })
    else:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_PASSWORD', })


# 根url入点
def ins(request):
    return HttpResponse('already logged')


# 注册
def register(request):
    try:
        register_data = simplejson.loads(request.body)
        print(register_data)
    except:
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
    if exist_tel_check(register_data['phone']):
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_tel_USED', })
    if not register_data['email'] and not mail_check(register_data['email']):
        return JsonResponse({'success': False, 'exc': 'ACCOUNT_EMAIL_USED', })
    n_user = models.User()
    n_user.u_tel = register_data['phone']
    n_user.u_name = register_data['name']
    n_user.u_passwd = hash_code(register_data['password'])
    n_user.u_email = register_data['email']
    n_user.u_sex = register_data['sex']
    n_user.u_type = register_data['type']
    n_user.u_age = register_data['age']
    n_user.u_intro = register_data['intro']
    n_user.save()
    return JsonResponse({'success': True, 'exc': '', })


def getMyInfo(request):
    if request.method == 'GET':
        try:
            user = models.User.objects.get(u_id=request.session['user_id'])
            package = {
                'success': True,
                'exc': '',
                'data': userToJson(user),
            }
            return JsonResponse(package)
        except:
            package = {
                'success': False,
                'exc': 'ACCOUNT_NOT_LOGGEDIN',
            }
            return JsonResponse(package)


def userToJson(user):
    ret = {}
    if(user == None):
        return None
    try:
        ret = {
            "id": user.u_id,
            "name": user.u_name,
            "phone": user.u_tel,
            "email": user.u_email,
            "type": user.u_type,
            "password": user.u_passwd,
            "avatar": user.u_avatar.url,
            "sex": user.u_sex,
            "age": user.u_age,
            "intro": user.u_intro,
        }
        return ret
    except:
        ret = {
            "id": user.u_id,
            "name": user.u_name,
            "phone": user.u_tel,
            "email": user.u_email,
            "type": user.u_type,
            "password": user.u_passwd,
            "avatar": "none",
            "sex": user.u_sex,
            "age": user.u_age,
            "intro": user.u_intro,
        }
        return ret


def uploadAvatar(request):
    if request.POST:
        uid = request.POST['id']
        try:
            user = models.User.objects.get(u_id=uid)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_404', })
        try:
            img_file = request.FILES.get("avatar")
        except:
            return JsonResponse({'success': False, 'exc': 'AVATAR_FORM_FAIL', })
        try:
            user.u_avatar = img_file
            user.save()
        except:
            return JsonResponse({'success': False, 'exc': 'UPLOAD_FAIL'})

        return JsonResponse({'success': True, 'exc': '', 'data': user.u_avatar.url})
    return JsonResponse({'success': False, 'exc': 'POSTONLY'})


def getAllUsers(request):
    if(request.method == "GET"):
        allusers = models.User.objects.all()
        ret = []
        for user in allusers:
            ret.append(userToJson(user))
    return JsonResponse({'success': True, 'exc': '', 'data': ret})


def update(request):
    if (request.method == "POST"):
        try:
            data = simplejson.loads(request.body)
        except:
            return JsonResponse({'success': False, 'exc': 'ACCOUNT_WRONG_FORMAT', })
        n_user = models.User.objects.get(u_id=data["id"])
        n_user.u_tel = data['phone']
        n_user.u_name = data['name']
        n_user.u_email = data['email']
        n_user.u_sex = data['sex']
        n_user.u_type = data['type']
        n_user.u_age = data['age']
        n_user.u_intro = data['intro']
        if(data['password']!=''):
            n_user.password = hash_code(data['password'])
        n_user.save()
    return JsonResponse({'success': True, 'exc': '', })
