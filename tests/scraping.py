from koth import scrape
import os
import shutil


def scraping1():
    '''
    Tests scraping on an old challenge from PPCG.
    '''
    print('Starting scraping test:')
    url = (
        'https://codegolf.stackexchange.com/questions/195032/totally-blind-'
        'chess'
    )
    if 'bots' in os.listdir():
        shutil.rmtree('bots')
    os.mkdir('bots')
    files = scrape(url)
    print('Scraped {} scripts.'.format(len(files)))
    print('Scraping test complete.')


if __name__ == '__main__':
    scraping1()
