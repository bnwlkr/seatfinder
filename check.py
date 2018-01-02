from bs4 import BeautifulSoup
import urllib3
import re
from getpass import getpass
from notifier import Notifier

courseURL = input("course url: ")
email = input("email address: ")
password = getpass('email password:')

http = urllib3.PoolManager()
r = http.request('GET', courseURL)
soup = BeautifulSoup(r.data, "lxml")

html = (soup.find_all('strong'))
generalseats = list(filter(lambda x: not (x==''),map(lambda x: re.sub('[a-zA-Z></: ]', '', str(x)), html)))[2]

if generalseats > 0:
    Notifier.notify(email, password, courseURL)