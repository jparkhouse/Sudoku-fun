from sudoku import Sudoku
from rsolve import solve
import numpy as np
import random
import time

x = Sudoku()
with open("sudokus.txt","r") as file:
    contents = file.read().split("\n")
#print(contents)
restimes = []
rrestimes = []
#while len(contents) > 0:
#    next = random.choice(contents)
#    x.inputFromFile(next)
#    contents.remove(next)
#    start = time.time()
#    x.solveByRecursion()
#    end = time.time()
#    times.append(end - start)
#    print("The average time taken is {0} and the total time taken is {1}".format(np.round(sum(times)/len(times),3),np.round(sum(times),3)))

for i in contents:
    x.inputFromFile(i)
    start = time.time()
    x.solveByRecursion()
    end = time.time()
    restimes.append(end - start)
    print("The average time taken for the recursive method is {0} and the total time taken is {1}".format(np.round(sum(restimes)/len(restimes),3),np.round(sum(restimes),3)))
    x.inputFromFile(i)
    start = time.time()
    x.solveByRRecursion()
    end = time.time()
    rrestimes.append(end - start)
    print("The average time taken  for the random recursion method is {0} and the total time taken is {1}".format(np.round(sum(rrestimes)/len(rrestimes),3),np.round(sum(rrestimes),3)))


#x.inputFromFile(".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8")
#x.solveByRecursion()
#x = Sudoku("111111111111111111111111111111111111111111111111111111111111111111111111111111...")
