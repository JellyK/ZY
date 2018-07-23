from django.http import HttpResponse, JsonResponse
from .models import UserAccess
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
import requests

import random
import string
import time

APP_ID = 'wxae99ab29ecc93d7c'
APP_SECRET = '4f9aa6b044ca2c610ce388a63ea2e8e1'
AUTH_CODE = 'authorization_code'
WX_GET_SESSION_URL = 'https://api.weixin.qq.com/sns/jscode2session'
WX_GET_SESSION_PARAMS = {
    'appid': APP_ID,
    'secret': APP_SECRET,
    'js_code': '',
    'grant_type': AUTH_CODE
}

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# session_key = ''
# openid = ''

def login(request):
    #url login is get user's session_key and openid and create User and UserAccess info
    # global session_key, openid
    code = request.GET.get('code')
    errMsg = request.GET.get('errMsg')
    print(code)
    print(errMsg)
    if not errMsg == 'login:ok':
        print('login error')
        return JsonResponse({'path': '/login',
                         'status': 'error',
                         'reason': errMsg})

    start = time.time()
    #request session_key and openid
    WX_GET_SESSION_PARAMS['js_code'] = code
    res = requests.get(WX_GET_SESSION_URL, params=WX_GET_SESSION_PARAMS)
    j = res.json()
    # api = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)
    # session_info = api.exchange_code_for_session_key(code=code)
    # print('session_info:' + session_info)
    session_key = j['session_key']
    openid = j['openid']
    print('session_key:' + session_key)
    print('openid:' + openid)
    print('time:{}'.format(time.time() - start))

    # openid = '111'
    start = time.time()

    userlist = User.objects.filter(username=openid)
    if userlist.count() == 0:
        # if there is no user info in table auth_user, create it
        user = User.objects.create_user(openid, password=User.objects.make_random_password())
    else:
        user = userlist[0]
    # if there is no user info in table user_access, create it
    user_access, is_created = UserAccess.objects.get_or_create(username=openid)
    print(user_access)

    #check session_key is same as it in userAccess or not
    if is_created or session_key != user_access.session_key:
        #create jwt by user
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user_access.session_key = session_key
        user_access.token = token
        user_access.save()
    else:
        token = user_access.token
    print('token:' + token)
    print('time2:{}'.format(time.time() - start))
    return JsonResponse({'path': '/login',
                         'status': 'ok',
                         'token': token})

def user(request):
    # use POST
    #url user is get the user's wxUserInfo, and
    print(request.method)
    print(request.POST)
    errMsg = request.POST.get('errMsg')
    print()
    if errMsg != 'getUserInfo:ok':
        return HttpResponse('failed to getUserInfo')
    rawData = request.POST.get('rawData')
    signature = request.POST.get('signature')
    encryptedData = request.POST.get('encryptedData')
    iv = request.POST.get('iv')
    token = request.POST.get('token')
    print('rawData: ' + rawData)
    print('signature: ' + signature)
    print('encryptedData: ' + encryptedData)
    print('iv: ' + iv)
    print('token: ' + token)
    try:
        user_access = UserAccess.objects.get(token=token)
        print('testtest:' + user_access.username)
    except UserAccess.objects.model.DoesNotExist:
        return JsonResponse({'path': '/user',
                             'status': 'error',
                             'reason': 'lack of token'})

    crypt = WXBizDataCrypt(APP_ID, user_access.session_key)
    userInfo = crypt.decrypt(encryptedData, iv)
    print(userInfo)
    return JsonResponse({'path': '/user',
                         'status': 'ok',
                         })

def random_password():
    src = string.ascii_letters + string.digits
    password = random.sample(src, 8)
    random.shuffle(password)
    return ''.join(password)