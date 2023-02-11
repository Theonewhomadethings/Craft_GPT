import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.lovelycraft.com/crochet-bunny-moo-amigurumi-pdf-pattern/')
 
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
# Getting the title tag
print(soup.title)
 
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)
 
# use the child attribute to get
# the name of the child tag

s = soup.find('div', class_='entry-content')

lines = s.find_all(['p', "h2", "h3"])
 
for line in lines:
    print(line.text)
