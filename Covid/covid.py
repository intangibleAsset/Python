#!/usr/bin/env python3

import utils
import datetime
import time

SCRAPED_DATA = "/home/anon/Python/Covid/data" # the scraped data
ACCESSED_TIME_FILE = "/home/anon/Python/Covid/last_accessed" # file containing datetime for last time data scraped

if utils.checked_in_last_hour(ACCESSED_TIME_FILE):
    print(utils.read_from_file(SCRAPED_DATA))
    print('read from file')
else:
    cases = utils.scrape_confirmed_cases("https://covid19.gov.im/general-information/latest-updates/")
    print(cases)
    utils.write_to_file(cases,SCRAPED_DATA)
    now = datetime.datetime.now()
    utils.write_to_file(str(datetime.datetime.timestamp(now)),ACCESSED_TIME_FILE)
    print('read from web')

"""

now = datetime.datetime.now()

utils.write_to_file(str(datetime.datetime.timestamp(now)), ACCESSED_TIME_FILE)

#convert file contents to float then int or you get an error
time = datetime.datetime.fromtimestamp(int(float(utils.read_from_file(ACCESSED_TIME_FILE))))

print(time)


today = datetime.datetime.now().date()

print(str(today))

print(utils.scrape("https://covid19.gov.im/general-information/latest-updates/"))


file_stat = os.stat(FILE_NAME)
mod_time = file_stat.st_mtime
difference = ((time.time() - mod_time) / 60)
time_mins = round(difference)

print(difference)
"""



"""
if time_mins < 2:
    print(utils.read_from_file(FILE_NAME))
    print('from file')
else:
    number = utils.scrape("https://covid19.gov.im/general-information/latest-updates/")
    print(number)
    print('from web')
    utils.write_to_file(number,"count")
"""
