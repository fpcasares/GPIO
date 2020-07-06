# Create a CommandSet for your remote control
# GPIO for the IR receiver: 15
# GPIO for the IR transmitter: 15
from ircodec.command import CommandSet
import json


JSON_FILE='AC.json'


def send_command(command,device_type='AC',emitter_gpio=14,receiver_gpio=15):
    controller = CommandSet(name=device_type, emitter_gpio=emitter_gpio, receiver_gpio=receiver_gpio, description=device_type)
    #Load from JSON:
    controller = CommandSet.load('{}.json'.format(device_type))
    controller.emit(command) 


def main():
    import time
    #Print contenct of the commands for the file
    json_obj=json.load(open(JSON_FILE,'rt'))
    for command in json_obj['commands'].keys():
        print(command)
    send_command('on')
    time.sleep(2)

    send_command('calor')
    time.sleep(2)
 
    send_command('25grados')
    time.sleep(2)


if __name__=='__main__':
    main()







