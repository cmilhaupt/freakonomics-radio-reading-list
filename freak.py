#! /usr/bin/python3

import urllib3
from bs4 import BeautifulSoup as bs

FREAKONOMICS_ARCHIVE_URL = 'http://freakonomics.com/archive/'

def get_links(r):
    soup = bs(r.data, 'html.parser')
    table = soup.find('table')
    tr = table.find_all('tr')
    tr = tr[1:]
    links = [t.find_all('a')[0]['href'] for t in tr]
    return links   

def get_books(link):
    r = http.request('GET', link)
    soup = bs(r.data, 'html.parser')
    divs = soup.find_all('div', attrs={'style': 'background-color: #eaeaea; padding: 10px;'})
    div = divs[0]
    ul = div.find(text='EXTRA').parent.parent.next_sibling.next_sibling
    li = ul.find_all('li')
    for l in li:
        if 'Freakonomics Radio' not in l.text:
            print(l.text)
    

def main(http):
    r = http.request('GET', FREAKONOMICS_ARCHIVE_URL)

    links = get_links(r)
    for link in links:
        books = get_books(link)

if __name__ == "__main__":
    http = urllib3.PoolManager()
    main(http)
