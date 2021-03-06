#!/usr/bin/python

import lcddriver
import re
from time import *
from subprocess import check_output

# Get first IP address using "hostname -I" command
ip = check_output(['hostname', '-I'])
m = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', ip)
if m is not None:
    ip = m.group(0)
else:
    ip = 'Not connected'

# Get local time
starttime = strftime("%H:%M:%S", localtime())

# Show on display
lcd = lcddriver.lcd()
lcd.lcd_display_string("Raspberry PI 2", 1)
lcd.lcd_display_string("", 2)
lcd.lcd_display_string('IP: ' + ip, 3)
lcd.lcd_display_string('Started at: ' + starttime, 4)

