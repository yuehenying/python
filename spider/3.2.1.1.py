#coding:utf-8
'''
import urllib2
response = urllib2.urlopen('http://www.zhihu.com')
html = response.read()
print html
'''

'''
import urllib2
#请求
request = urllib2.Request('http://www.zhihu.com')
response = urllib2.urlopen(request)
html = response.read()
print html
'''

# POST请求
import urllib
import urllib2
url = 'http://localhost/login.php'
postdata = {
    'username': 'admin',
    'password': 'admin'
}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data)
resposne = urllib2.urlopen(req)
html = resposne.read()
print html