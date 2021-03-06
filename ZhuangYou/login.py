from django.http import HttpResponse
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
import requests
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
import random,string
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
    #create and add user into db
    userlist = User.objects.filter(username=openid)
    if userlist.count() == 0:
        user = User.objects.create_user(openid, password=random_password())
    else:
        user = userlist[0]
    print(user)

    print('time2:{}'.format(time.time() - start))

    #create jwt by user
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    print('token:' + token)
    return HttpResponse('login successfully')

def user(request):
    # data = request.GET.
    print(request.method)
    if request.method == 'GET':
        print('rawData' + request.GET.get('rawData'))
    elif request.method == 'POST':
        print('rawData' + request.POST.get('rawData'))
    crypt = WXBizDataCrypt(APP_ID, session_key)
    print('crypt:' + crypt.__str__())
    return HttpResponse("hello world")

def random_password():
    src = string.ascii_letters + string.digits
    password = random.sample(src, 8)
    random.shuffle(password)
    return ''.join(password)