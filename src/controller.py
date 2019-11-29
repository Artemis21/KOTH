import pexpect


class Player:
    def __init__(self, cmd):
        self.proc = pexpect.spawn(cmd)
        self.proc.send('###GAME START###\n')
        self.proc.expect_exact('###GAME START ACK###')

    def turn(self, inp):
        self.proc.send('===INPUT START===\n')
        self.proc.send(inp)
        self.proc.send('===INPUT END===\n')
        self.proc.expect_exact('===OUTPUT START===')
        self.proc.expect_exact('===OUTPUT END===')
        return self.proc.before.decode('utf-8').strip()

    def end(self):
        self.proc.send('###GAME END###\n')
        self.proc.expect_exact('###GAME END ACK###')
        self.proc.terminate(force=True)

