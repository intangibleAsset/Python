import requests
from bs4 import BeautifulSoup
import datetime

def get_page(url):
    """Use requests to get page data with fake header."""
    headers = {'user-agent': 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    r = requests.get(url, headers=headers)
    return(r.text)

def get_crime_links(page):
    """Return list of headline 'a' tags appended with iomtoday."""
    soup = BeautifulSoup(page, 'lxml')
    links = []
    for headlines in soup.find_all('article', class_="story story--list"):
        links.append('http://www.iomtoday.co.im/'+headlines.header.h2.a['href'])
    return(links)

def get_article_text(link):
    page = get_page(link)
    soup = BeautifulSoup(page,'lxml')
    text = []
    article = soup.find('article', class_ = "story u-clearfix")
    text.append(article.h1.getText())
    p = article.find_all('p')
    for all in p:
        text.append(all.getText())        

    return(text)
