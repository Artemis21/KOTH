from koth import Client


class TestBot(Client):
    def setup(self):
        self.n = 0

    def turn(self, inp):
        self.n += 1
        return '{}: {}'.format(self.n, inp)


TestBot()
