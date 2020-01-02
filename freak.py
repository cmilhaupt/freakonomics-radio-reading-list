#! /usr/bin/python3

import argparse
import urllib3
from urllib.parse import urlparse
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
    book_list = {}

    r = http.request('GET', link)
    soup = bs(r.data, 'html.parser')
    podcast_intro = soup.find_all('div', attrs={'class': 'podcast_intro'})
    ll_links = podcast_intro[0].find_all('a')
        
    for link in ll_links:
        if 'amazon' in link['href']:
            o = urlparse(link['href'])
            book_list[o.path.split('/')[3]] = link
    
    for key in book_list.keys():
        print(key)    
    return book_list        

def main(http):
    parser = argparse.ArgumentParser(description='Freakonomics Book List Scraper')
    parser.add_argument('-a', '--all', 
                        action='store_true',
                        help='Changes \'most recent\' modifier to \'all\' \
                        for -t, -l, and -p arguments')
    parser.add_argument('-l', '--links',
                        action='store_true',
                        help='View most recent link(s)')
    parser.add_argument('-t', '--transcripts',
                        action='store_true',
                        help='Download most recent transcript(s)')
    parser.add_argument('-p', '--process',
                        action='store_true',
                        help='Extract most recent book(s)')
    parser.add_argument('-f', '--full',
                        action='store_true',
                        help='Equivalent to -ltp')
    args = parser.parse_args()

    if args.full is True:
        args.links = True
        args.transcripts = True
        args.process = True
   
    # r = http.request('GET', FREAKONOMICS_ARCHIVE_URL)
    # links = []
    # if args.links is True:
    #     links = get_links(r, args.all)

    # argparse
    # download archive page, symmetric difference of url list
    # download new pages, spacy works of art on text
    # Save url list to github pages in comments 
    # Publish <a href> list from original transcript
    
    # podcast_intro = soup.find_all('div', attrs={'class': 'podcast_intro'})
    # all_links = podcast_intro[0].find_all('a')
    # all_href = [link['href'] for link in podcast_intro[0].find_all('a')]
    # 
    # 
    # nlp = spacy.load('en_core_web_sm')
    # doc = nlp(podcast_intro[0].text)
    # 
    # for end in doc.ents:
    #     if 'WORK_OF_ART' in ent.label_:
    #         print(ent.text, ent.start_char, ent.end_char, ent.label_)

    r = http.request('GET', FREAKONOMICS_ARCHIVE_URL)
    book_list = {}

    links = get_links(r)
    for link in links:
        books = get_books(link)
        break
        if books is not None:
            print(books.keys())
            book_list.update(get_books(link))

    f = open('docs/index.html', 'w+')
    for _, value in book_list.values():
        f.write(value)
        f.write('\n')
    f.close()

if __name__ == "__main__":
    http = urllib3.PoolManager()
    main(http)
