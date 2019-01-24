# coding:utf-8
'''
# 判断是否重定向
import urllib2
response = urllib2.urlopen('http://www.zhihu.cn/')
isRedirected = response.geturl() == 'http://www.zhihu.cn/'
print isRedirected
'''

# 自定义HTTPRedirectHandler类
import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result
opener = urllib2.build_opener(RedirectHandler)
response = opener.open('http://www.zhihu.cn/')
print response.read()