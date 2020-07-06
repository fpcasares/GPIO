# Create a CommandSet for your remote control
# GPIO for the IR receiver: 23
# GPIO for the IR transmitter: 22
from ircodec.command import CommandSet
controller = CommandSet(name='AC',emitter_gpio=14, receiver_gpio=15, description='AC')

#Load from JSON:
controller = CommandSet.load('AC.json')


# Add the volume up key
#controller.add('turn_on_off')
# Connected to pigpio
# Detecting IR command...
# Received.

# Send the volume up command
controller.emit('turn_on_off')

# Remove the volume up command
#controller.remove('volume_up')

# Examine the contents of the CommandSet
#controller
# CommandSet(emitter=22, receiver=23, description="TV remote")
# {}

# Save to JSON
#controller.save_as('AC.json')

# Load from JSON
