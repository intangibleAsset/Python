#!/usr/bin/env python3

import scrape
import file
import datetime


if file.accessed_in_last_hour():
    html = file.read_from_file('page')
    print('reading from file')
else:
    html = scrape.get_page('http://www.iomtoday.co.im/archive.cfm?sectionIs=News&cat=Crime')
    print('reading live sight and saving to file system')

crime_links = scrape.get_crime_links(html)

print(scrape.get_article_text(crime_links[0]))
