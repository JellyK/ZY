from django.http import HttpResponse
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt

APP_ID = 'wxae99ab29ecc93d7c'
APP_SECRET=''

def login(request):
    code = request.GET.get('code')
    errMsg = request.GET.get('errMsg')

    api = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)
    session_info = api.exchange_code_for_session_key(code=code)

    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(APP_ID, session_key)

    return HttpResponse("hello world")