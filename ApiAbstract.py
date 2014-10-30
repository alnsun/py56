from urllib import urlencode
from hashlib import md5
import time

class ApiAbstract(object):
    '''
    author: Allan Sun <email: alnsun.cn@gmail.com;QQ:301585>
    '''

    DOMAIN = 'http://oapi.56.com'
    APPKEY = ''
    SECRET = ''

    def __init__(self):
        self.domain = self.DOMAIN
        self.appkey = self.APPKEY
        self.secret = self.SECRET

    def setConf(self, **conf):
        self.appkey = conf['appkey']
        self.secret = conf['secret']
        return self

    def get_http(self, url, **params):
        pass

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
