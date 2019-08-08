import sudoku
from copy import deepcopy as dc
from random import shuffle
best = (0,0)
digits = [1,2,3,4,5,6,7,8,9]
def solve(grid):
    global best
    grid = dc(grid)
    tosolve = solved(grid)
    if tosolve == True:
        best = (0,0)
        return grid
    else:
        if tosolve[1] > best[1]:
            best = tosolve
            #print("the furthest solution so far has gotten to {0}/81, or {1}% complete".format(best[0] + best[1] * 9,int(((best[0] + best[1] * 9)/81)*100)))
        elif tosolve[1] == best[1] and tosolve[0] > best[0]:
            best = tosolve
            print("the furthest solution so far has gotten to {0}/81, or {1}% complete".format(best[0] + best[1] * 9,int(((best[0] + best[1] * 9)/81)*100)))
        for i in range(1,10):
            if checker(tosolve[0],tosolve[1],i,grid):
                grid[tosolve[1]][tosolve[0]] = i
                x = solve(grid)
                if x != None:
                    if solved(x) == True:
                        best = (0,0)
                        return x
    #print("Box ({0},{1}) is unsolvable, backtracing...".format(tosolve[0],tosolve[1]))

def rsolve(grid):
    global best
    global digits
    grid = dc(grid)
    d = dc(digits)
    shuffle(d)
    tosolve = solved(grid)
    if tosolve == True:
        best = (0,0)
        return grid
    else:
        if tosolve[1] > best[1]:
            best = tosolve
            #print("the furthest solution so far has gotten to {0}/81, or {1}% complete".format(best[0] + best[1] * 9,int(((best[0] + best[1] * 9)/81)*100)))
        elif tosolve[1] == best[1] and tosolve[0] > best[0]:
            best = tosolve
            print("the furthest solution so far has gotten to {0}/81, or {1}% complete".format(best[0] + best[1] * 9,int(((best[0] + best[1] * 9)/81)*100)))
        for i in d:
            if checker(tosolve[0],tosolve[1],i,grid):
                grid[tosolve[1]][tosolve[0]] = i
                x = solve(grid)
                if x != None:
                    if solved(x) == True:
                        best = (0,0)
                        return x
    #print("Box ({0},{1}) is unsolvable, backtracing...".format(tosolve[0],tosolve[1]))

def checker(x,y,n,grid):
    #generate 3x3 box
    if x < 3:
        xcoords=[0,1,2]
    elif x < 6:
        xcoords=[3,4,5]
    else:
        xcoords=[6,7,8]
    if y < 3:
        ycoords=[0,1,2]
    elif y < 6:
        ycoords=[3,4,5]
    else:
        ycoords=[6,7,8]
    box=[]
    for j in ycoords:
        for i in xcoords:
            box.append(grid[j][i])
    #generate row and column
    row=[]
    column=[]
    for i in range(0,9):
        row.append(grid[y][i])
        column.append(grid[i][x])
    blist=[]
    if n in box:
        blist.append("")
    if n in row:
        blist.append("")
    if n in column:
        blist.append("")
    if len(blist) > 0:
        return False
    else:
        return True

def solved(grid):
    tosolve = False
    for row in grid:
        if tosolve == False:
            for i in row:
                if i == " " and tosolve == False:
                    tosolve = (row.index(i),grid.index(row))
    if tosolve == False:
        return True
    else:
        return tosolve