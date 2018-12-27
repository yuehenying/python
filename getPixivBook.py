import requests
from bs4 import BeautifulSoup
import re

links = []
names = []
page = 1
proxy = '127.0.0.1:25378'   #自己设置代理服务器地址
localPath = r'E:\pictures\P站\\'  #图片保存的路径
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'cookie': 'first_visit_datetime_pc=2018-12-07+20%3A44%3A50; p_ab_id=3; p_ab_id_2=2; p_ab_d_id=1308768103; PHPSESSID=24852177_3159d4223485c13802ada647bbb51686; device_token=38b9553872ea1daf403b59ba896b134a; privacy_policy_agreement=1; c_type=23; a_type=0; b_type=1; yuid_b=hYGUUFA; login_ever=yes; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; ki_s=193385%3A0.0.0.0.0; __utmz=235335808.1544686486.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=24852177=1^9=p_ab_id=3=1^10=p_ab_id_2=2=1^11=lang=zh=1; __utma=235335808.2062136180.1544686486.1544686486.1544692049.2; ki_r=; ki_t=1544183255645%3B1545212898808%3B1545212949576%3B10%3B25; limited_ads=%7B%22illust_responsive%22%3A%22%22%2C%22responsive%22%3A%22%22%7D; categorized_tags=1DJe5jv-kK~CADCYLsad0~IVwLyT8B6k~OEXgaiEbRa~OT-C6ubi9i~b8b4-hqot7; is_sensei_service_user=1; user_language=zh; tags_sended=1; tag_view_ranking=BU9SQkS-zU~y8GNntYHsi~RTJMXD26Ak~0xsDLqCEW6~Lt-oEicbBr~NpsIVvS-GF~jH0uD88V6F~KN7uxuR89w~MfZareoazp~J1ZxtWenHC~C4Nv34WiSc~tslFWUOajq~4Ctmr5n26O~rZKyhUz9Lf~i83OPEGrYw~gooMLQqB9a~azESOjmQSV~q3eUobDMJW~l2rugVKl6u~aUKGRzPd6e~1HSjrqSB3U~AAEyK1fN5m~xZ6jtQjaj9~vRR5qN4-In~ve2_ejdUqn~pYlUxeIoeg~QfHe9Nt5we~_SsgZaf_zV~aUbeMF-jdb~gpglyfLkWs~Ie2c51_4Sp~faHcYIP1U0~fg8EOt4owo~ueeKYaEKwj~ajFGI2BXvo~28gdfFXlY7~L58xyNakWW~zyKU3Q5L4C~wx98zZNxJM~r70NVOGJ5H~kGYw4gQ11Z~Cj_Gcw9KR1~tgP8r-gOe_~FFBbSsTrOz~-oGijJmC5S~kkoONtHi_j~q303ip6Ui5~aNqTPYQ7NR~Bd2L9ZBE8q~cbmDKjZf9z~K8esoIs2eW~kwQ7-a01CG~An9WzWRM2w~MSNRmMUDgC~1Y_znGjU36~BQv9ZOKrJ7~0Sds1vVNKR~OT4SuGenFI~lQ7gBjqCjC~o0HD1XpAtx~biEwLEAGY3~YS9AMUnAgS~xjfPXTyrpQ~ftZLeIHm13~PHsucBd84t~DcMFRkXx6k~Rcy15Dsiti~4Dp_oH0cTU~EWHQU2eNa6~E8plmQ7kUK~144zWY--zX~R0YfWwQKL0~IfTHG7cZ8v~yqqObNqIba~MO67n2Zm2e~bdsHaxGhC9~NDsKQx4TRT~_k4KvXUPsw~MM6RXH_rlN~iFcW6hPGPU~uC2yUZfXDc~RcahSSzeRf~AXY26q50qc~81BOcT1ZAV~lo0hog5Ml-~5f1R8PG9ra~CiSfl_AE0h~qykC9T3TS5~OY7CQOs1pO~sB7901Amvc~CLlequVPZC~hzDjKGXB1A~tU-DeosfDN~LtW-gO6CmS~oYAm9klH0r~kP7msdIeEU~nQRrj5c6w_~i_dZaon0j6~etIk2CNMvk~r1vRjXa1Om', #自己的cookie
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'
}
proxies = {
    'https': proxy
}
def download():
    global page,url
    url = 'https://www.pixiv.net/bookmark.php?rest=show&p='+str(page)
    res = requests.get(url = url,headers = headers,proxies = proxies)
    soup = BeautifulSoup(res.text,'html.parser')
    linkList = soup.select('._layout-thumbnail .ui-scroll-view')
    titleList = soup.select('.image-item .title') 

    for link in linkList:
        link = link['data-src'].replace('c/150x150/','')
        links.append(link)

    for t in titleList:
        t = t['title'].replace('/','')
        names.append(t)
    
    if page < 5:
        page = page + 1
        download()
    
def savePicture():
    for (pic,name) in zip(links,names):
        res = requests.get(url = pic,headers = headers,proxies = proxies)
        with open(localPath+name+'.jpg','wb') as f:
            f.write(res.content)
            print(name+'下载完毕')

download()
savePicture()
