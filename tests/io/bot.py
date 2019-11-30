'''
Test/example usage of the "client-side" wrapper for bot/controller interaction.
'''
from koth import Client


class TestBot(Client):
    '''
    A simple bot that returns a number followed by the input it recieved. The
    number starts at one and increments each time.
    '''
    def setup(self):
        # We increment the count *before* returning it, so set it as 0 not 1.
        self.n = 0

    def turn(self, inp):
        # Return the number and input.
        self.n += 1
        return '{}: {}'.format(self.n, inp)


# Run the bot.
TestBot()
