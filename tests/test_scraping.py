from koth import scrape
import os
import shutil
import unittest


class TestScraping(unittest.TestCase):
    def setUp(self):
        if 'bots' in os.listdir():
            shutil.rmtree('bots')
        os.mkdir('bots')

    def tearDown(self):
        shutil.rmtree('bots')

    def test_scraping(self):
        '''
        Tests scraping on an old challenge from PPCG.
        '''
        url = (
            'https://codegolf.stackexchange.com/questions/195032/totally-'
            'blind-chess'
        )
        files = scrape(url)
        self.assertTrue(len(files) > 0)
        self.assertTrue(files[0].startswith('bots/'))


if __name__ == '__main__':
    unittest.main()
