'''
Test/example usage of the "server-side" wrapper for bot/controller interaction,
prints input and output to/from the bot.
'''
from koth import Player
import traceback


def io1():
    '''
    I/O test to make sure the bot returns values as it should, with three
    inputs: a simple string, a multi-line string and the empty string.
    '''
    print('Starting I\O test 1 (basic):')
    # Start the bot.
    bot = Player('python3 bot.py')
    for i in 'test', 'multi\nline', '':
        # Tell the bot to respond to each input.
        ret = bot.turn(i)
        print('Sent input "{}", recieved output "{}".'.format(i, ret))
    # Kill the bot.
    bot.end()
    print('I\O Test 1 complete.')


def io2():
    '''
    I/O test to make sure it handles timeout correctly. The 1st bot waits for
    5 seconds before making a move but we set a 2 second timeout. The 2nd bot
    never sends GAME START ACK, and the third bot works normally and we set a
    5 second timeout.
    '''
    print('Starting I\O test 2 (timeout):')
    print('Starting I\O test 2.1 (turn timeout):')
    bot = Player('python3 bot2.py', wait=2)
    ret = bot.turn('test')
    print('Sent input "test", recieved output "{}".'.format(ret))
    bot.end()
    print('I\O test 2.1 complete.')
    print('Starting I\O test 2.2 (start timout):')
    try:
        bot = Player('python3 bot3.py')
        print('No error!')
        bot.end()
    except Exception:
        print('Error:')
        print(traceback.format_exc())
    print('I\O test 2.2 complete.')
    print('Starting I\O test 2.3 (no timeout):')
    bot = Player('python3 bot.py', wait=5, gamewait=1)
    ret = bot.turn('a')
    ret2 = bot.turn('b')
    bot.end()
    print('Returns: {}, {}.'.format(ret, ret2))
    print('I\O test 2.3 complete.')
    print('I\O test 2 complete.')


if __name__ == '__main__':
    io1()
    io2()
