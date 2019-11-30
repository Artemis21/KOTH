class Client:
    def __init__(self):
        inp = ''
        while inp != '###GAME START###':
            inp = input()
        self.setup()
        print('###GAME START ACK###')
        self._listen()

    def _listen(self):
        stop = False
        while not stop:
            stop = self._signal()
        self.cleanup()
        print('###GAME END ACK###')

    def _signal(self):
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

    def setup(self): pass

    def cleanup(self): pass

    def turn(self, inp):
        raise NotImplementedError('The turn function must be implemented.')
