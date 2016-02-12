#!/usr/bin/python
#-- coding:utf-8 --

import codecs
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250/'

html = requests.get(DOWNLOAD_URL).content

soup = BeautifulSoup(html)

movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

movie_name_list = []

for movie_li in movie_list_soup.find_all('li'):
    movie_name = movie_li.find('span', attrs={'class': 'title'}).getText()
    movie_name_list.append(movie_name)


for movie_name in movie_name_list:
	print movie_name

