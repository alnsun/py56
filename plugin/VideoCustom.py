from py56 import ApiAbstract

class VideoCustom(ApiAbstract):
    '''
    sid
    css
    rurl
    ourl
    return plugin
    '''
    #def __init__(self):
    #    super(VideoCustom, self).__init__()

    def get(self, **param):
        url = '%s%s' % (self.domain, '/video/custom.plugin')
        print param
        return '%s?%s' % (url, self.signRequest(**param))
