#!/usr/bin/env python3

import scrape
import file
import datetime


if not file.accessed_in_last_hour():
    print('*** reading live sight and saving to file system ***')
    html = scrape.get_page('http://www.iomtoday.co.im/archive.cfm?sectionIs=News&cat=Crime')
    crime_links = scrape.get_crime_links(html)
    articles_text_list = []
    for art in crime_links:
        articles_text_list.append(scrape.get_article_text(art))
    file.pickle_object(articles_text_list,"articles_text_list")

else:
    print('*** reading from file ***')
    articles_text_list = file.unpickle_object('articles_text_list')
    print(articles_text_list)
