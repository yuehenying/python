import re
import urllib

class HtmlParser(object):

    def parser(self, page_url, html_content):
        '''
        解析json文件提取图片url和名字
        param page_url:下载页面的url
        param html_content: 下载的网页内容
        return: 返回URL和数据
        '''
        if page_url is None or html_content is None:
            return None
        new_urls = self._get_new_urls(page_url, html_content)
        return new_urls


    def _get_new_urls(self, page_url, html_content):
        new_urls = set()
        pictures = re.findall(r'https://i0.hdslb.com/bfs/album/\w+\.(?:jpg|png)', html_content)
        for pic in pictures:
            new_urls.add(pic)
        return new_urls

        