'''
import urllib
import urllib2
url = 'http://localhost/login.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://localhost/'
postdata = {
    'username': 'admin',
    'password': 'admin'
}
headers = {'User-Agent': user_agent, 'Referer': referer}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
html = response.read()
print html
'''

import urllib
import urllib2
url = 'http://localhost/login.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://localhost/'
postdata = {
    'username': 'admin',
    'password': 'admin'
}
data = urllib.urlencode(postdata)
req = urllib2.Request(url)
req.add_header('User-Agent', user_agent)
req.add_header('referer', referer)
req.add_data(data)
response = urllib2.urlopen(req)
html = response.read()

