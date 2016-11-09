#!/usr/bin/env python

import time, sys
import datetime
import libPiLite as lpl

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

serial = lpl.PiLiteSerial()

tickcount = 0

while True:
    if tickcount == 30:
        grid = lpl.createBlankGrid(9,14)
        grid = clockFace(grid, datetime.datetime.now().time())
        print ""
        #lpl.printGrid(grid) #for debugging only
        tickcount = 0
    else:
        if (tickcount%2)==0:
            grid = lpl.setGrid(grid,[[0,1],[0,3]],0,0)
        else:
            grid = lpl.resetGrid(grid,[[0,1],[0,3]],0,0)
        tickcount += 1
            
    serial.writeBinary(lpl.serializeGrid(grid))
    time.sleep(1)
