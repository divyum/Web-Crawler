Python Crawler
==============

Link Crawler
---------------------
The Python script **link_crawler.py** is a simple python crawler which crawls all the links present in a webpage. The user provides the **URL** of the page to be crawled for the links, in the **command line**. The code will print all the links present in the page.
I have taken guidance from udacity course for making and understanding the code. It is very useful for the beginners to understand the code.

packages required:

- urllib2
- sys

Syntax

$ python link_crawler.py *URL*

**$ python link_crawler.py http://xkcd.com/**

RSS Crawler
---------------------
The Python script **rss_crawler.py** is a simple python crawler which crawls all the news headlines of a rss page of any news website. The user provides the **URL** of the rss to be crawled for the news, in the **command line**. The code will print all the **News Headlines** present in the RSS feed of the page.

packages required:

- urllib2
- sys
- string
- re
- collections

Syntax

$ python rss_crawler.py *URL*

**$ python rss_crawler.py http://timesofindia.feedsportal.com/c/33039/f/533965/index.rss**

