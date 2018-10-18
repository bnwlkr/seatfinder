from bs4 import BeautifulSoup
import urllib3
import re
from getpass import getpass
from notifier import Notifier
import time


courseURL = input("course url: ")
email = raw_input("email address: ")
password = getpass('email password:')

http = urllib3.PoolManager()
generalseats = 0

while generalseats == 0:
    time.sleep(5)
    r = http.request('GET', courseURL)
    soup = BeautifulSoup(r.data, "lxml")
    html = (soup.find_all('strong'))
    generalseats = list(filter(lambda x: not (x==''),map(lambda x: re.sub('[a-zA-Z></: ]', '', str(x)), html)))[2]
    print ("still no seats :(")


Notifier.notify(email, password, courseURL)
