#constains with default value
import logging
debugging_level = logging.ERROR                 #setting up logging level (debug, info, warning, error)

#setter for debug lvl
def set_debugging_level(level):
    if(level == "debug"):
        debugging_level = logging.DEBUG

    if(level == "info"):
        debugging_level == logging.INFO

    if(level == "warning"):
        debugging_level == logging.WARNING

    if(level == "error"):
        debugging_level == logging.ERROR
    return

#getter for debug level
def get_debugging_level():
    return debugging_level
