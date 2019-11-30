from koth import Player


print('Starting I\O test:')
bot = Player('python3 bot.py')
for i in 'test', 'multi\nline', '':
    ret = bot.turn(i)
    print('Sent input "{}", recieved output "{}".'.format(i, ret))
bot.end()
print('Test complete.')
