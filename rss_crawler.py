"""This file is a RSS parser. It reads the source of a news website RSS URL and displays all the news headlines of the RSS. """

import urllib2
import sys
import string
import re
from collections import OrderedDict

#escape punctuations
chars = re.escape(string.punctuation)

def get_source(page):
    url=urllib2.urlopen(page)
    source=url.read()
    return source

def get_page(page):
    url=urllib2.urlopen(page)
    source=url.read()
    return source

#function that stores the start point and the end point of news
def get_next_target(page):
        start_title1 = page.find('<title')
        start_link1 = page.find('<link',start_title1 + 1)
        start_desc1 = page.find('<description', start_link1 + 1)
        start_pubdate1 = page.find('<pubDate',start_desc1 + 1)
        if start_title1==-1 or start_link1==-1 or start_desc1==-1 or start_pubdate1==-1:
            return None,None,None,None,0
        start_title = page.find('>',start_title1 + 1)
        start_link = page.find('>',start_link1 + 1)
        start_desc = page.find('>',start_desc1 + 1)
        if (page[start_desc+2]=='!'):
            start_desc = page.find('[',start_desc + 1)
            if (page[start_desc+1]=='<'):
                start_desc = page.find('/>',start_desc + 1)                
        start_pubdate = page.find('>',start_pubdate1+1)
        end_title = page.find('</title>', start_title + 1)
        end_link = page.find('</link>', start_link + 1)
        i=0
        if(page.find('</description>',start_desc + 1)>0):
            temp1=page.find('</description>',start_desc + 1)
        if(page.find('&lt',start_desc + 1)>0):
            temp1=min(temp1,page.find('&lt',start_desc + 1))
        if(page.find('<',start_desc + 1)>0):
            temp1=min(temp1,page.find('<',start_desc + 1))
        end_desc = temp1
        end_pubdate = page.find('</pubDate>',start_pubdate + 1)
        url = page[start_title + 1:end_title]
        url=re.sub(r'['+chars+']', ' ',url)
        url.replace("CDATA"," ")
        link = page[start_link + 1:end_link]
        desc = page[start_desc + 1:end_desc]
        desc=re.sub(r'['+chars+']', ' ',desc)
        desc=desc.replace("CDATA"," ")
        pubDate = page[start_pubdate + 1:end_pubdate]
        if url and link and desc and pubDate:
            return url,link,desc,pubDate,end_pubdate
        else:
            return None,None,None,None,0

#function that appends the news to a list
def get_all_links(page):
    links=[]
    while True:
        url, link, desc, pubDate, endpos= get_next_target(page)
        if url and link and desc and pubDate:
            links.append(url)
            page = page[endpos:]
        else:
            break;
    return links

links=get_all_links(get_source(sys.argv[1]))

#It removes duplicate news
links= list(OrderedDict.fromkeys(links))

for i in range(len(links)):
	print links[i]
