import requests
r = requests.get('https://www.baidu.com')
if r.status_code == 200:
    print r.status_code
    print r.headers
    print r.headers.get('Date')
    print r.headers['content-type']
else:
    r.raise_for_status()  #抛出异常