import requests
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        headers = {
            'User-Agent': user_agent
        }
        res = requests.get(url, headers = headers)
        if res.status_code == 200:  
            return res.text

   