#!/usr/bin/python3

import subprocess
import threading
from time import sleep
import logging
import poniclog
from datetime import datetime

now = str(datetime.now())

while True:
        try:
            logging.info(now)
            logging.info('start myponic')
            subprocess.call(["python3", "/home/pi/Desktop/myponic-main/port.py"])
            print("reset")
        except Exception as e:
            print(e)
            logging.info(now)
            logging.info('RESET')
            logging.info('--------------------------------------------------------------------------------------------------------')
        sleep(50)