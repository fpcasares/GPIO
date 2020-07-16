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





# BCM GPIO for the IR transmitter: 14
GPIO_EMITTER=14
# BCM GPIO for the IR receiver: 15
GPIO_RECEIVER=15

JSON_FILE='./ir_codes/AC.json'

'''
def load(self):
    """Try to load all IR CODES found in the ir_codes folder"""
    ir_codes = []
    path = os.path.join(os.path.dirname(__file__), "ir_codes")
    directory = pkgutil.iter_modules(path=[path])
    for finder, name, ispkg in directory:
        try:
            loader = finder.find_module(name)
            module = loader.load_module(name)
            if hasattr(module, "commandWords") \
                    and hasattr(module, "moduleName") \
                    and hasattr(module, "execute"):
                self.modules.append(module)
                print("The module '{0}' has been loaded, "
                      "successfully.".format(name))
            else:
                print("[ERROR] The module '{0}' is not in the "
                      "correct format.".format(name))
        except:
            print("[ERROR] The module '" + name + "' has some errors.")
    print("\n")
'''



def send_command(command,file=JSON_FILE,device_type='AC',emitter_gpio=GPIO_EMITTER,receiver_gpio=GPIO_RECEIVER):
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
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--available-commands", help="Show available lists of IR commands",action="store_true")
    parser.add_argument("-c","--command",type=str, help="Command to send to AC")
    #parser.add_argument("-irc","--ir-commands",type=str, help="Command to send to AC")
    args = parser.parse_args()
    
    if args.available-commands:
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
