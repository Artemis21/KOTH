class Client:
    '''
    "Client-side" wrapper for the interaction. Should be inherited by Python
    bots, which should override turn, and optionally setup and cleanup.
    __init__ should *not* be overwritten, instead use setup.
    '''
    def __init__(self):
        '''
        Wait for the game to start, setup the bot, acknowledge the game
        starting (tells the controller that it is ready), then listen for
        turns. This function is will run until the game ends.
        '''
        inp = ''
        while inp != '###GAME START###':
            inp = input()
        self.setup()
        print('###GAME START ACK###')
        self._listen()

    def _listen(self):
        '''
        Internal event loop to listen for signals, call the appropriate methods
        then return the appropriate responses.
        '''
        stop = False
        while not stop:
            stop = self._signal()
        self.cleanup()
        print('###GAME END ACK###')

    def _signal(self):
        '''
        Internal method to wait for a signal, handle it and return the response
        to stdout. Returns True if the game is over, False otherwise.
        '''
        i = ''
        while i != '===INPUT START===':
            i = input()
            if i == '###GAME END###':
                return True
        inp = ''
        i = ''
        while i != '===INPUT END===':
            inp += i + '\n'
            i = input()
        inp = inp.strip()
        print('===OUTPUT START===')
        print(self.turn(inp))
        print('===OUTPUT END===')
        return False

    def setup(self):
        '''
        Dummy function, called when the game starts. Optionally may be
        implemented by bots to set up stuff. No return.
        '''

    def cleanup(self):
        '''
        Dummy function, called when the game ends. Optionally may be
        implemented by bots to clean up after themselves. No return.
        '''

    def turn(self, inp):
        '''
        Dummy function, called when it is the bot's turn. Must be implemented,
        should return whatever the challenge specifies as the ouput of a turn.
        '''
        raise NotImplementedError('The turn function must be implemented.')
