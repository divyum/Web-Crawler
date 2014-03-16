import urllib2
import sys

#list to store URLs crawled from the webpage
url_list=[]

#function that returns source code of URL
def get_source(page):
    url=urllib2.urlopen(page)
    source=url.read()
    return source

#function that finds the start point and end point of each link present in the page.
def get_next_target(page):
    start_link=page.find('<a href="http')
    end_link=page.find('"',start_link+10)
    if start_link==-1 or end_link==-1:
        return None,None
    url = page[start_link+9:end_link]
    return url,end_link

#function that appends the link in list
def get_all_links(page):
    while True:
        url,end_link = get_next_target(page)
        if url:	
	    url_list.append(url)
            page = page[end_link+4:]
        else:
            break

#page contains the source code of URL entered by the user in command line
page=get_source(sys.argv[1])
get_all_links(page)

#prints all the links stored in list
for i in range(len(url_list)):
	print url_list[i]
