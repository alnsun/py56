```
In [1]: from py56.video import VideoCustom

In [2]: v = VideoCustom(appkey='xxx', secret='xxx')

In [3]: v.get(css='cDElM0RwMSUyNnAyJTNEcDIlMjZvbiUzRG9uJTI2b24lM0RvbiUyNm9uJTNEb24lMjZwbyUzRHBvJTI2bCUzRGNuJTI2YyUzRHAxMSUyNmklM0Qx', ourl='http://domain.net', rurl='http://domain.net', sid=1)

Out[3]: 'http://oapi.56.com/video/custom.plugin?appkey=xxx&ourl=http%3A%2F%2Fdomain.net&ts=1414654240&sign=ee0113c66a6cc328270157aaa979ca5c&sid=1&rurl=http%3A%2F%2Fdomain.net&css=cDElM0RwMSUyNnAyJTNEcDIlMjZvbiUzRG9uJTI2b24lM0RvbiUyNm9uJTNEb24lMjZwbyUzRHBvJTI2bCUzRGNuJTI2YyUzRHAxMSUyNmklM0Qx'
```
