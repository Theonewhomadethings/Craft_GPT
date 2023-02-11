# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import csv
from cleantext import clean


links = []
with open('links.csv', newline='', encoding='ANSI') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for link in reader:
        links.append(link)


for link in links[0]:
    print("####################################################")
    print(link)
    # Making a GET request
    try:
        r = requests.get(link)
    except:
        next
    
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
    
    text = ""
    for line in lines:
        text += line.text + "\n"
        print(line.text)
    title = soup.title.text.replace('"','')

    with open(f'patterns/{title}.txt', 'w+') as f:
        f.write(clean(text, no_emoji=True))
