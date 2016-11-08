#!/usr/bin/env python

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
            
