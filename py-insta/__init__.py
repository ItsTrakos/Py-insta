
"""
# -*- coding: utf-8 -*-
__author__ = "Trakos"
__email__ = "mhdeiimhdeiika@gmail.com"
__version__ = 1.0.0"
__copyright__ = "Copyright (c) 2019 -2021 Leonard Richardson"
# Use of this source code is governed by the MIT license.
__license__ = "MIT"
Description:
            py-Insta Is A Python Library
  
            Scrape Instagram Data
            And Print It Or You Can Define It Into A Variable...
#####
__version__ = 1.0
import requests
from bs4 import BeautifulSoup

__url__ = "https://www.instagram.com/{}/"

def Insta(username):
    try:
        response = requests.get(__url__.format(username.replace('@','')),timeout=5)  # InCase Someone Types @UserName
        if '404' in str(response):  # If The Username Is Invalid
            data = 'No Such Username'
            return data
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            meta = soup.find("meta", property="og:description")
            try:
                s = meta.attrs['content'].split(' ')
                data = {
                    'Followers': s[0],
                    'Following': s[2],
                    'Posts': s[4],
                    'Name': s[13]
                }
                return data
            except requests.exceptions.InvalidURL:
                return 'No Such Username'
    except (requests.ConnectionError, requests.Timeout):
        return 'No InterNet Connection'