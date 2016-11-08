#!/usr/bin/env python

import serial
import time, sys

class PiLiteSerial:
    def __init__(self):
        self.s = serial.Serial()
        self.s.baudrate = 9600
        self.s.timeout = 0
        self.s.port = "/dev/serial0"
        self.open()
        self.write("$$$ALL,OFF\r")

    def open(self):
        try:
            self.s.open()
        except serial.SerialException, e:
            sys.stderr.write("Could not open port %r: %s\n" % (self.s.port, e))
            sys.exit(1)

    def write(self, msg):
        self.s.write(msg)

    def writeBinary(self, msg):
        msg = "$$$F"+msg+"\r"
        self.s.write(msg)

def createBlankGrid(row,column):
    blankgrid = [[0 for x in range(column)] for y in range(row)]
    
    return blankgrid

def getHeight(grid):
    return len(grid)

def getWidth(grid):
    return len(grid[0])

def printGrid(grid):
    numRow = len(grid)
    for i in range(0,numRow):
        row = grid[i]
        rowstr = ''
        for j in row:
            rowstr += str(j)+' '
        print(rowstr)

def serializeGrid(grid):
    numRow = len(grid)
    numCol = len(grid[0])
    gridstr = ''
    for j in range(0,numCol):
        for i in range(0,numRow):
            gridstr += str(grid[i][j])
    return gridstr

def setGrid(grid, setlist, rowoffset, coloffset):
    for entry in setlist:
        grid[entry[0]+rowoffset][entry[1]+coloffset] = 1
    return grid

def resetGrid(grid, setlist, rowoffset, coloffset):
    for entry in setlist:
        grid[entry[0]+rowoffset][entry[1]+coloffset] = 0
    return grid
