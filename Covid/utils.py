import requests
from bs4 import BeautifulSoup
import datetime

def check_last_update(file_name):
    """Check_last_update(file_name)."""
    file_stat = os.stat(file)
    mod_time = file_stat.st_mtime
    difference = ((time.time() - mod_time) / 60)
    return difference

def read_from_file(file_name):
    """Read_from_file(file_name)."""
    with open(file_name,"r") as file:
        amount = file.read()
    return(amount)

def write_to_file(data, file_name):#writes the file contents to the file overwriting the last update
    with open(file_name,"w") as file:
        file.write(data)

def checked_in_last_hour(file_name):
    value = False
    accessed_time = datetime.datetime.fromtimestamp(int(float(read_from_file(file_name))))
    accessed_time_plus_one_hour = accessed_time + datetime.timedelta(minutes=60)
    if datetime.datetime.now() < accessed_time_plus_one_hour:
        value = True
    return value

def scrape_confirmed_cases(url):#scrapes covid numbers from the iom government web page
    headers = {'user-agent': 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    r = requests.get(url, headers=headers)
    main_page = r.text
    soup = BeautifulSoup(main_page, 'html.parser')
    text_list = soup.text.split('\n')
    index = 0

    for i in range(0,len(text_list)):
        if text_list[i] == 'Confirmed cases':
            index = i

    index = index + 1
    return(text_list[index])
