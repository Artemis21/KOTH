'''
Test usage of the "client-side" wrapper for bot/controller interaction. Never
finishes setting up.
'''
from koth import Client
import time


class TestBot(Client):
    '''
    A simple bot that never finishes setting up.
    '''
    def setup(self):
        while True:
            time.sleep(100)

    def turn(self, inp):
        return "I'm not ready :("


# Run the bot.
TestBot()
