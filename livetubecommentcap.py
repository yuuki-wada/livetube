# coding:utf-8

import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("http://livetube.cc/%E3%81%92%E3%81%87%E3%83%BC%E3%81%8F/201507010315")

soup = BeautifulSoup(html)

target = soup.find_all("span", style="cursor: pointer")
for i in xrange(len(target)):
        text = target[i].get_text()
        text = BeautifulSoup(text)
        text = text.p.wrap(soup.new_tag("div"))
        print text

