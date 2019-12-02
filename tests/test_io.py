'''
Test/example usage of the "server-side" wrapper for bot/controller interaction.
'''
from koth import Player
import re
import unittest


class TestIO(unittest.TestCase):
    def test_simple_io(self):
        '''
        I/O test to make sure the bot returns values as it should, with three
        inputs: a simple string, a multi-line string and the empty string.
        '''
        # Start the bot.
        bot = Player('python3 io/bot.py')
        for i in 'test', 'multi\nline', '':
            # Tell the bot to respond to each input.
            ret = bot.turn(i)
            with self.subTest(i=i):
                self.assertTrue(ret)
                self.assertEqual(ret[3:], i)
        # Kill the bot.
        bot.end()

    def test_timeout_io(self):
        '''
        I/O test to make sure it handles timeout correctly. The 1st bot waits
        for 5 seconds before making a move but we set a 2 second timeout. The
        2nd bot never sends GAME START ACK, and the third bot works normally
        and we set a 5 second timeout.
        '''
        with self.subTest(bot='bot2.py'):
            bot = Player('python3 io/bot2.py', wait=2)
            ret = bot.turn('test')
            # None means no output recieved.
            self.assertEqual(ret, None)
            bot.end()
        with self.subTest(bot='bot3.py'):
            with self.assertRaises(TimeoutError):
                bot = Player('python3 io/bot3.py')
                bot.end()
        with self.subTest(bot='bot.py'):
            bot = Player('python3 io/bot.py', wait=5, gamewait=1)
            ret = bot.turn('a')
            ret2 = bot.turn('b')
            self.assertTrue(ret)
            self.assertTrue(ret2)
            bot.end()


if __name__ == '__main__':
    unittest.main()
