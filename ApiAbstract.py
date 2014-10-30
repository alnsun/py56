from urllib import urlencode
from hashlib import md5
import time

try:
    from local_config import *
except:
    from config import *

class ApiAbstract(object):
    '''
    author: Allan Sun <email: alnsun.cn@gmail.com;QQ:301585>
    '''

    def __init__(self, **kwargs):
        self.domain = DOMAIN
        self.appkey = APPKEY
        self.secret = SECRET

    def setConf(self, **kwargs):
        if 'appkey' in kwargs:
            self.appkey = kwargs['appkey']
        if 'secret' in kwargs:
            self.secret = kwargs['secret']
        if 'domain' in kwargs:
            self.domain = kwargs['domain']

    def signRequest(self, **params):
        kv_list = params.items()
        kv_list.sort()

        req = md5(urlencode(kv_list)).hexdigest()
        ts = int(time.time())

        params['appkey'] = self.appkey
        params['sign'] = md5('#'.join([req, self.appkey, self.secret, str(ts)])).hexdigest()
        print 'sign=', params['sign']
        params['ts'] = str(ts)
        return urlencode(params)
