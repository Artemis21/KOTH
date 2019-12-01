'''
Test usage of the "client-side" wrapper for bot/controller interaction which
waits for 5 seconds before sending response to a turn.
'''
from koth import Client
import time


class TestBot(Client):
    '''
    A simple bot that waits 5 seconds before sending turn.
    '''
    def turn(self, inp):
        time.sleep(5)
        return '5 seconds later...'


# Run the bot.
TestBot()
