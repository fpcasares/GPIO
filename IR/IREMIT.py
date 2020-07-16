# Create a CommandSet for your remote control

import os
if os.system('ps -A | grep pigpiod >>/dev/null')==0:
    GPIO=False
    try:
        from ircodec.command import CommandSet
    except:
        quit()
else:
    quit()
    

import json
import glob




# BCM GPIO for the IR transmitter: 14
GPIO_EMITTER=14
# BCM GPIO for the IR receiver: 15
GPIO_RECEIVER=15

JSON_FILE='./ir_codes_modules/AC.json'

def get_files():
    file_list=glob.glob('./GPIO/IR/ir_codes_modules/*')
    return (file_list)


def send_command(command,file=JSON_FILE,device_type='*',emitter_gpio=GPIO_EMITTER,receiver_gpio=GPIO_RECEIVER):
    controller = CommandSet(name=device_type, emitter_gpio=emitter_gpio, receiver_gpio=receiver_gpio, description=device_type)
    #Load from JSON:
    controller = CommandSet.load(file)
    controller.emit(command)
    
def get_available_commands(file=JSON_FILE):
    json_obj=json.load(open(file,'rt'))
    commands_list=list()
    return(list(json_obj['commands'].keys()))
    
    



def main():
    import time
    import random
    import argparse
    import configparser
    
    
    commands_list=get_available_commands()
    files=get_files()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--available-commands", help="Show available lists of IR commands",action="store_true")
    parser.add_argument("-c","--command",type=str, help="Command to send to AC")
    parser.add_argument("-f","--files", help="Available command_set files for a particular device", action="store_true")
    args = parser.parse_args()
    
    
    if args.files:
        for item in files:
            print(item)
    
    
    if args.available_commands:
        for item in commands_list:
            print(item)
    
    if args.command=='None':
        #Do a demo of the IR emit
        for index in range(0,3):
            command=commands_list[random.randint(0,len(commands_list)-1)]
            send_command(command)
    elif args.command in commands_list:
            send_command(args.command)

if __name__=='__main__':
    main()
