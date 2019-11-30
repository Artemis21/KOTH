'''
Test/example usage of the "server-side" wrapper for bot/controller interaction,
prints input and output to/from the bot.
'''
from koth import Player


print('Starting I\O test:')
# Start the bot.
bot = Player('python3 bot.py')
for i in 'test', 'multi\nline', '':
    # Tell the bot to respond to each input.
    ret = bot.turn(i)
    print('Sent input "{}", recieved output "{}".'.format(i, ret))
# Kill the bot.
bot.end()
print('Test complete.')
