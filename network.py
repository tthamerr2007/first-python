#!/usr/bin/env python3
import requests
def check_localhost():
 localhost = socket.gethostbyname('localhost')
 x = localhost
if x == '127.0.0.1':
 return True
def check_connectivity():
 request = requests.get("http://www.google.com")
 y = (request.status_code)
if y == 200:
 return True
