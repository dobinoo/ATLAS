#This is the core program
#This takes care of basically all input and output

import time                 #import for time use
import logging              #import for future debug

#main function
if __name__ == "__main__":

    #logging config - level (DEBUG,INFO,WARNING,ERROR)
    logging.basicConfig(filename = "/debug/debug.log", encoding = "utf-8", level = logging.DEBUG, format = "%(asctime)s %(message)s")

    #main loop bacially takes care of life, universe and everything (42)
    while True:
        text = input()
        time.sleep(3)
        print(text)
