class Client:
    def __init__(self):
        inp = ''
        while inp != '###GAME START###':
            inp = input()
        self.setup()
        print('###GAME START ACK###')
        self.listen()

    def listen(self):
        inp = ''
        while inp != '###GAME END###':
            i = ''
            while i != '===INPUT START===':
                i = input()
            inp = ''
            i = ''
            while i != '===INPUT END===':
                inp += i + '\n'
                i = input()
            inp = inp.strip()
            print('===OUTPUT START===')
            print(self.turn(inp))
            print('===OUTPUT END===')
        self.cleanup()
        print('###GAME END ACK###')

    def setup(self): pass

    def cleanup(self): pass

    def turn(self, inp):
        raise NotImplementedError('The turn function must be implemented.')
