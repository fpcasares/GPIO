# Create a CommandSet for your remote control
# GPIO for the IR receiver: 23
# GPIO for the IR transmitter: 22
from ircodec.command import CommandSet
controller = CommandSet(name='AC',emitter_gpio=14, receiver_gpio=15, description='AC')



# Add the keys
key=''

while key!='quit': 
    key=input('Enter the key name\n') 
    if key!='quit':
        controller.add(key)
     


# Save to JSON
file=input('Enter the device you want to store the keys (e.g. AC)\n')
controller.save_as('{}.json'.format(file))



