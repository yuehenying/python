#coding:utf-8
'''
# 获取cookie
import cookielib
import urllib2

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('https://www.zhihu.com')
for item in cookie:
    print item.name + ':' + item.value
'''

# 设置cookie
import urllib2
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'email=' + "xxxxxxx@163.com"))
req = urllib2.Request('https://www.zhihu.com/')
response = opener.open(req)
print response.headers
retdata = response.read()

