#!/usr/bin/env python3

import scrape
import file
import datetime

#url = 'http://www.iomtoday.co.im/archive.cfm?sectionIs=News&cat=Crime'

now = datetime.datetime.now()
last_accessed_time = file.unpickle_object('accessedTime')
if last_accessed_time < (now - datetime.timedelta(seconds=30)):
    file.pickle_object(now,'accessedTime')
    print('accessed over thirty seconds ago')
else:
    print('accessed less than thirty seconds ago')
