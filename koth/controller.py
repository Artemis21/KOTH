import pexpect


class Player:
    '''
    "Server-side" wrapper for the interaction. One should be created per bot,
    per game.
    '''
    def __init__(self, cmd):
        '''
        Spawn the bot process, send it GAME START and wait for GAME START ACK.
        This tells the bot to set up.
        '''
        self.proc = pexpect.spawn(cmd)
        self.proc.send('###GAME START###\n')
        self.proc.expect_exact('###GAME START ACK###')

    def turn(self, inp):
        '''
        Give the bot input and tell it to take its turn, return its output.
        '''
        self.proc.send('===INPUT START===\n')
        self.proc.send(inp + '\n')
        self.proc.send('===INPUT END===\n')
        self.proc.expect_exact('===OUTPUT START===')
        self.proc.expect_exact('===OUTPUT END===')
        return self.proc.before.decode('utf-8').strip()

    def end(self):
        '''
        Tell the bot the game is over, let it clean up then kill it.
        '''
        self.proc.send('###GAME END###\n')
        self.proc.expect_exact('###GAME END ACK###')
        self.proc.terminate(force=True)
