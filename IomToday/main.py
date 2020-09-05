#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import datetime

#url = 'http://www.iomtoday.co.im/archive.cfm?sectionIs=News&cat=Crime'

#headers = {'user-agent': 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
#r = requests.get(url, headers=headers)
#main_page = r.text

file_name = 'page'
#with open(file_name,"w") as file:
#    file.write(main_page)

with open(file_name,"r") as file:
    page = file.read()

#soup = BeautifulSoup(page, 'html.parser')
soup = BeautifulSoup(page, 'lxml')
print(soup.find_all('a'))

#soup.find('div',class='')



#with open(file_name,"r") as file:
#    amount = file.read()

#text_list = soup.text.split('\n')

#for i in text_list:#print entire page to console as text with newlines
#    print(str(i)+'\n')

#index = 0

#for i in range(0,len(text_list)):
#    if text_list[i] == 'Confirmed cases':
#        index = i
#    print(text_list[index])
#
#    index = index + 1
#    print(text_list[index])
