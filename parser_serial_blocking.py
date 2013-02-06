#/usr/bin/env python

#browserzacken google-chrome logfile parser based on shockenzocken parser

# ugly simple ioURT parser for shockenzacken/painoverTCP by scriptythekid 2012-2013
# mostly based on:
#	 ioUrT Parser for BigBrotherBot(B3) (www.bigbrotherbot.net)
#	 Copyright (C) 2008 Mark Weirath (xlr8or@xlr8or.com)
#

#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

#
#
#run: python parser.py <logfile> <serialdevice>
#

#FIXME throw this away and write a bigbrotherbot plugin... 

import re
import sys
import fileinput
import time
import serial

try:
  serdev = sys.argv[2]
  ser = serial.Serial(serdev, 9600)
except Exception, e:
  print "could not open", serdev
  sys.exit(1)

fd = open(sys.argv[1], 'r')
print "opened ",sys.argv[1]
#seek to end of file
fd.seek(0,2)
print "seeked to end of file, pos:", fd.tell()
print
print "make sure to add a blocked cookie config in the browserextension!"
print
print "WARNGING player/shockhandle ID hardcoded to 0"
print 
#sys.exit(1)

while True:
  for line in fd.readlines():
    line = line.strip() 		#remove leading/trailing whitespace so regexes match...!
    line = re.sub(timerex, '', line, 1)	#remove leading minutes/secs from logLine
    
    if 'SHOCKENZACKEN' in line:
      shockcmd='S%d1-A.' % int(0)
      ser.write(shockcmd)
      print "sending",shockcmd


    else:
      #print "no regex match for this line:"
      #print line
      pass
   
  #ugly way to reduce IO load otherwise this script takes up 100% CPU ...
  time.sleep(0.01)
  
  


