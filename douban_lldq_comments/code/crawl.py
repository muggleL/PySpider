import requests
import re

from time import sleep
from code.config import HEADERS, COOKIES, RE_CONTENT


def get_page_content(url):
    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    response.encoding = 'utf-8'
    return response.text


def get_content(html):
    re_content = re.compile(RE_CONTENT, re.S)
    content = re.findall(re_content, html)
    return content


def crawl():
    page = 0
    base_url = 'https://movie.douban.com/subject/26266893/comments?start='
    while True:
        html = get_page_content(base_url + str(page))
        content = get_content(html)
        if not content:
            break
        print("got " + str(page + 20) + " comments success!")
        yield content
        if page == 480:
            page = 490
        else:
            page += 20
        sleep(1)
