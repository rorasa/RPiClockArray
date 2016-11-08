#!/usr/bin/env python

#import serial
import time, sys
import datetime
import libPiLite as lpl

#s = serial.Serial()
#s.baudrate = 9600
#s.timeout = 0
#s.port = "/dev/serial0"

#try:
#    s.open()
#except serial.SerialException, e:
#    sys.stderr.write("Could not open port %r: %s\n" % (s.port, e))
#    sys.exit(1)
#
#s.write("$$$ALLL,OFFF\r")
#time.sleep(0.5)

#while True:
#    currenttime = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
#    
#    s.write(currenttime+"\r")
#    time.sleep(1)

numberprofile = { 0: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4]],
                  1: [[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,4]],
                  2: [[0,0],[0,1],[0,2],[0,4],[1,0],[1,2],[1,4],[2,0],[2,2],[2,3],[2,4]],
                  3: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,2],[1,4],[2,0],[2,2],[2,4]],
                  4: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,2],[2,0],[2,1],[2,2]],
                  5: [[0,0],[0,2],[0,3],[0,4],[1,0],[1,2],[1,4],[2,0],[2,1],[2,2],[2,4]],
                  6: [[0,0],[0,2],[0,3],[0,4],[1,0],[1,2],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4]],
                  7: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[2,0]],
                  8: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,2],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4]],
                  9: [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,2],[1,4],[2,0],[2,1],[2,2],[2,4]] }

def clockFace(grid, currenttime):
    hour = currenttime.hour
    minute = currenttime.minute
    
    # set hour display
    if hour < 10:
        hourlist = numberprofile[hour]
        rowoffset = 4
        coloffset = 0
        grid = lpl.setGrid(grid,hourlist,rowoffset,coloffset)
    else:
        if hour < 20:
            hourlist = numberprofile[1]
        else:
            hourlist = numberprofile[2]
        rowoffset = 6
        coloffset = 0
        grid = lpl.setGrid(grid,hourlist,rowoffset,coloffset)
        
        hourlist = numberprofile[hour%10]
        rowoffset = 2
        coloffset = 0
        grid = lpl.setGrid(grid,hourlist,rowoffset,coloffset)

    # set minute display
    minutelist = numberprofile[minute/10]
    rowoffset = 6
    coloffset = 6
    grid = lpl.setGrid(grid,minutelist,rowoffset,coloffset)

    minutelist = numberprofile[minute%10]
    rowoffset = 2
    coloffset = 6
    grid = lpl.setGrid(grid,minutelist,rowoffset,coloffset)
    
    return grid

currenttime = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M')
print currenttime

grid = lpl.createBlankGrid(9,14)
#lpl.printGrid(grid)

grid = clockFace(grid, datetime.datetime.now().time())

lpl.printGrid(grid)
