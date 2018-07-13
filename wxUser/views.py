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

session_key = ''
openid = ''

def login(request):
    global session_key, openid
    code = request.GET.get('code')
    errMsg = request.GET.get('errMsg')
    print(code)
    print(errMsg)
    if not errMsg == 'login:ok':
        print('login error')
        return HttpResponse('login error')

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

    start = time.time()
    # check user is in UserAccess db or not
    userlist = UserAccess.objects.filter(username=openid)
    if userlist.count() == 0:
        # if there is no user info in db, create it
        auth_user = User.objects.create_user(openid, password=random_password())
        user_access = UserAccess.objects.create(username=openid)
    else:
        user_access = userlist[0]
    print('time2:{}'.format(time.time() - start))

    #check session_key is
    #create jwt by user
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    user_access.session_key = session_key
    user_access.token = token
    user_access.save()
    print('token:' + token)
    return JsonResponse({'login': 'ok',
                         'token': token})

def user(request):
    # use POST
    print(request.method)
    print(request.POST)
    errMsg = request.POST.get('errMsg')
    if errMsg != 'getUserInfo:ok':
        return HttpResponse('failed to getUserInfo')
    rawData = request.POST.get('rawData')
    signature = request.POST.get('signature')
    encryptedData = request.POST.get('encryptedData')
    iv = request.POST.get('iv')
    print(rawData)
    print(signature)
    print(encryptedData)
    print(iv)

    crypt = WXBizDataCrypt(APP_ID, session_key)
    userInfo = crypt.decrypt(encryptedData, iv)
    print(userInfo)
    return HttpResponse("hello world")

def random_password():
    src = string.ascii_letters + string.digits
    password = random.sample(src, 8)
    random.shuffle(password)
    return ''.join(password)