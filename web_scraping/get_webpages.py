import requests
from bs4 import BeautifulSoup
import csv

links = []

page = 1
for page in range(1,49):
    # Making a GET request
    r = requests.get(f'https://www.lovelycraft.com/page/{page}/')
    
    # check status code for response received
    # success code - 200
    print(r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())
    # Getting the title tag
    # print(soup.prettify())
    
    # # Getting the name of the tag
    # print(soup.title.name)
    
    # # Getting the name of parent tag
    # print(soup.title.parent.name)
    
    # use the child attribute to get
    # the name of the child tag

    s = soup.find('div', class_='blog-listing-el')

    lines = s.find_all(['a'])
    
    for i, line in enumerate(lines):
        if i%2 == 0:
            links.append(line['href'])
            print(line['href'])

with open('links.csv', 'w', newline='') as csvfile:
    write = csv.writer(csvfile, delimiter=',')
    write.writerow(links)
 