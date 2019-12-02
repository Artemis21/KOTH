import pexpect


class Player:
    '''
    "Server-side" wrapper for the interaction. One should be created per bot,
    per game.
    '''
    def __init__(self, cmd, wait=2, gamewait=None):
        '''
        Spawn the bot process, send it GAME START and wait for GAME START ACK.
        This tells the bot to set up.
        Parameters:
         - cmd: the command to launch the bot, eg. `python3 bots/egbot.py`.
                Required.
         - wait: how long to wait for the bot to make a move, in seconds. 0
                 means forever. Default 2.
         - gamewait: how long to wait for the bot to set up/clean up, in
                     seconds. 0 means forever. Default None (whatever wait is).
        Raises:
         - TimeoutError: timed out waiting for GAME START ACK.
        '''
        if gamewait is None:
            gamewait = wait
        self.proc = pexpect.spawn(cmd, timeout=wait)
        self.proc.send('###GAME START###\n')
        ack = self.expect('###GAME START ACK###', gamewait)
        if not ack:
            raise TimeoutError('Bot timed out (command: {}).'.format(cmd))
        self.gamewait = gamewait

    def expect(self, arg, timeout=-1):
        '''
        Internal method to expect some output within a timeout (default set in
        __init__ with parameter wait).
        Parameters:
         - arg: the output to wait for, required.
         - timeout: how long to wait, in seconds. Default -1 (set in __init__).
        Returns:
        Boolean specifiying whether the output was recieved in time.
        '''
        try:
            self.proc.expect_exact(arg, timeout=timeout)
            return True
        except pexpect.TIMEOUT:
            return False

    def turn(self, inp):
        '''
        Give the bot input and tell it to take its turn, return its output.
        Parameters:
         - inp: the input to give the bot, required.
        Returns:
        None if the output was not recieved in time, otherwise the output.
        '''
        self.proc.send('===INPUT START===\n')
        self.proc.send(inp + '\n')
        self.proc.send('===INPUT END===\n')
        t = self.expect('===OUTPUT START===')
        if not t:
            return None
        t = self.expect('===OUTPUT END===')
        if not t:
            return None
        # \n becomes \r\n.
        return self.proc.before.decode('utf-8').replace('\r\n', '\n').strip()

    def end(self):
        '''
        Tell the bot the game is over, let it clean up then kill it. No
        parameters or returns.
        '''
        self.proc.send('###GAME END###\n')
        self.expect('###GAME END ACK###', self.gamewait)
        self.proc.terminate(force=True)
