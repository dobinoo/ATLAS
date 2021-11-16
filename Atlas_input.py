#This is the input part of ATLAS
#The part of ATLAS that take care of input
#Here the voice input is compared with specific sequences and it should forward the input to the right part of program

import time                         #import for time use
import logging                      #import for future debug

logging_level = logging.DEBUG       #setting up logging level
logging.basicConfig(filename = "debug/input.log", encoding = "utf-8", level = logging_level, format = "%(asctime)s %(message)s")     #logging config


#Main function to call in core program to parse voice
def voice_input(voice_sentence):
    logging.debug("Voice_input function with this sentence: " + voice_sentence + "\n")
    voice_output = "You are asking wrong question\n"
    logging.info("Setting default voice_output: " + voice_output + "\n")

    if voice_sentence == "ATLAS":
        voice_output = "Automated and Trustworthy Linear Analysis Subsystem"
        logging.debug("Returning voice_output: " + voice_output + "\n")

    return voice_output
