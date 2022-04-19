#This is the core program
#This takes care of basically all input and output

import time                         #import for time use
import logging                      #import for future debug
import Atlas_input                  #importing function to take care of input
#add later
######## import voice library       #importing voice library for ATLAS speaker

logging_level = logging.DEBUG       #setting up logging level
output = "Just testing output, this will change in future"          #just testing output - change in future

def exit_function():
    logging.debug("Ending the main process (core.py)\n")
    exit()
    return

#main function
if __name__ == "__main__":

    #logging config - level (DEBUG,INFO,WARNING,ERROR)
    logging.basicConfig(filename = "debug/debug.log", encoding = "utf-8", level = logging_level, format = "%(asctime)s %(message)s")
    logging.debug("Starting the main process (core.py)\n")

    #main loop basically takes care of life, universe and everything (42)
    while True:
        text = input()
        logging.debug("User input: " + text)

        if text == "exit":
            exit_function()

        #time.sleep(3) commenting just for now
        print("User input: " + text)
        #print("ATLAS output: " + output + "\n")
        print("ATLAS output: " + Atlas_input.voice_input(text) + "\n")

            ########################For Exception########################
            #print("Unknown Error") exception not working right now
            #logging.error("Unknown error, last constains :" + text) not working right now
            ######################################################################
