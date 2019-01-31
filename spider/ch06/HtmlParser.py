import re
import urllib
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, page_url, html_content):
        '''
        用于解析网页数据内容提取URL和数据
        :param page_url: 下载页面的url
        :param html_content: 下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_content is None:
            return 
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的url集合
        :param page_url: 下载页面的url
        :param soup: soup
        :return: 返回新url集合
        '''
        new_urls = set()
        #抽取符合要求的a标签
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        '''
        提取有效数据
        :param page_url:下载页面的url
        :param soup
        :return:返回有效的数据
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_= 'lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data
