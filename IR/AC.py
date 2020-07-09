# Imports

import argparse
import configparser
from IREMIT import *



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="Show debugging information", action="store_true")
    parser.add_argument("-c","--command",type=str, help="Command to send to AC")
    args = parser.parse_args()
    
    if not args.command:
        command='on'
    
    send_command(command)




if __name__ == '__main__':
    main()
       
    
