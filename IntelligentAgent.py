import random
import time
import math
from BaseAI import BaseAI

cur = None
start = None
class IntelligentAgent(BaseAI):   
    def getMove(self, grid):
    	# Selects a random move and returns it
        global start
        start = time.process_time()
        cur = Play(grid)
        if cur !=None and cur[0]!=None:
            return cur[0][0]
        else:
            return (grid.getAvailableMoves()).pop()[0]
    
def Play(grid) :
    move = None
    alpha = -10000000
    beta =   10000000
    i = 1
    while 1 :
        global cur
        j=0
        cur = maximize((move,grid),alpha,beta,i,j)
        if time.process_time()-start>.195:
            return cur
        i = i+1
    
    
def minimize(state,alpha,beta,i,j):
    global cur
    if j>=i:
        return (None,Eval(state))
    
    (minChild, minUtility) = (None,10000000)
    j = j+1 
    
    
    if time.process_time()-start>.195:
        return cur
    
    
    for pos in state[1].getAvailableCells():
        
        if time.process_time()-start>.195:
            return cur
        
        
        child = state[1].clone()
        child2 = state[1].clone()
        child.insertTile(pos,2)
        child2.insertTile(pos,4)
        maxim = maximize((None, child),alpha,beta,i,j)
        maxim2 = maximize((None, child2),alpha,beta,i,j)
        utility = .9*maxim[1] + .1*maxim2[1]
        
        if utility < minUtility:
            (minChild,minUtility) = (state[1],utility)
                
        if minUtility<=alpha:
            break
            
        if minUtility<beta:
            beta = minUtility
                
    return (minChild,minUtility)
        
def maximize(state,alpha,beta,i,j):
    if j>=i:
        return (None,Eval(state))
    (maxChild, maxUtility) = (None,-10000000)
    j = j+1 
    
    
    if time.process_time()-start>.195:
        return cur
    
    
    for child in state[1].getAvailableMoves():
        
        if time.process_time()-start>.195:
            return cur
    
    
        child[1].move(child[0])
        minim = minimize((None, child[1]),alpha,beta,i,j)
        utility = minim[1]
        
        if utility > maxUtility:
            (maxChild,maxUtility) = (child,utility)
                
        if maxUtility>=beta:
            break
            
        if maxUtility>alpha:
            alpha = maxUtility  
            
    return (maxChild,maxUtility)
    
def Eval(state):
    #heuristics based off of the article given
    
    emptyWeight = math.log(len(state[1].getAvailableCells())+1) * 2.7
    maxWeight = state[1].getMaxTile()
    monotonicity = mono(state[1])
   
    return emptyWeight + maxWeight + monotonicity

def mono(grid): 
    # This code was converted by me into python from the javascript implementation used by the other team
    totals = [0,0,0,0]
    
    for i in range(4):
        current =0
        Next = current +1
        while Next<4:
            while Next < 4 and grid.map[i][Next]==0:
                Next = Next+1
            if Next>=4:
                Next = Next-1
            currentValue = grid.map[i][current]
            if currentValue!=0:
                currentValue = math.log(currentValue/math.log(2))
            nextValue = grid.map[i][Next]
            if nextValue!=0:
                nextValue = math.log(nextValue/math.log(2))
            if currentValue > nextValue:
                totals[0] += nextValue - currentValue
            elif nextValue > currentValue:
                totals[1] += currentValue - nextValue
            current = Next
            Next = Next + 1
            
    ##converted code
    for i in range(4):
        current =0
        Next = current +1
        while Next<4:
            while Next < 4 and grid.map[Next][i]==0:
                Next = Next+1
            if Next>=4:
                Next = Next-1
            currentValue = grid.map[current][i]
            if currentValue!=0:
                currentValue = math.log(currentValue/math.log(2))
            nextValue = grid.map[Next][i]
            if nextValue!=0:
                nextValue = math.log(nextValue/math.log(2))
            if currentValue > nextValue:
                totals[2] += nextValue - currentValue
            elif nextValue > currentValue:
                totals[3] += currentValue - nextValue
            current = Next
            Next = Next + 1
    
    return max(totals[0],totals[1]) + max(totals[2],totals[3])