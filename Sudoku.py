import numpy as np
from time import time
import matplotlib.pyplot as plt
#from scipy.optimize import linprog

def Check_Puzzle(sol):
	isCorrect = True
	for i in range(len(sol)):
		if len(np.unique(sol[i])) != len(sol[i]): #checks across rows
			isCorrect = False
			break
		elif len(np.unique(sol[:,i])) != len(sol[:,i]): #checks down rows
			isCorrect = False
			break
			
		p1 = 0; p2 = 0;
		for j in range(9):
			if np.size(sol[p1:p1+3,p2:p2+3]) != len(np.unique(sol[p1:p1+3,p2:p2+3])): #checks each 3x3 box
				isCorrect = False
				break
			if j == 2 or 5:
				p1 += 3
			p2 = (p2+3)%9

	return isCorrect





def Make_Puzzle(initNum): #init should be the number of initial starting points (shouldn't be less than 17)
	base  = 3
	side  = base*base

	# pattern for a baseline valid solution
	def pattern(r,c): return (base*(r%base)+r//base+c)%side #// is floor(division())

	# randomize rows, columns and numbers (of valid base pattern)
	from random import sample
	def shuffle(s): return sample(s,len(s)) 
	rBase = range(base) 
	rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
	cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
	
	nums  = shuffle(range(1,base*base+1))

	# produce board using randomized baseline pattern
	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

	#for line in board: print(line)
	squares = side*side
	empties = 81 - initNum #squares * 3//4

	for p in sample(range(squares),empties):
	    board[p//side][p%side] =0 #np.nan
	sol = np.array(board)
	numSize = len(str(side))
	return sol
	
def Convert_Puzzle(puz):
	if np.shape(puz) == (729,):
		sol = np.zeros([9,9])
		for i in range(729):
			if puz[i] < 1 + 1e-9 and puz[i] > 1 - 1e-9:
				sol[int(np.floor(i/9)%9), int(np.floor(i/81))] = (i%9)+1
		return(np.transpose(sol))


def DirSum(a,r):
        dsum = np.zeros([np.shape(a)[0]*r,np.shape(a)[1]*r])
        for i in range(r):
            k = np.shape(a)[0]*i
            l = np.shape(a)[1]*i
            dsum[k:k+np.shape(a)[0],l:l+np.shape(a)[1]]=a
        return(dsum)

def Make_Aconst():
	iRow = np.tile(np.eye(9),9)
	Arow = DirSum(iRow,9)
    
	az = DirSum(np.eye(9),9)
	Acol = np.tile(az,9)
    
	J = np.tile(np.eye(9),3)
	Abox = DirSum(np.tile(DirSum(J,3),3),3)

	Acell = DirSum(np.ones([1,9]),81)
    
	Aconst = np.vstack([Arow,Acol,Abox,Acell])
	return(Aconst)

'''
def Convert_Puzzle(puz): #check dimension and return the opposite!
	#if np.shape(puz) == (9,9,9):
	print(np.shape(puz))
	puzl = puz.astype(int)
	sol = np.zeros([9,9])
	tracker = 0
	for k in range(9):
		for j in range(9):
			for i in range(9):
				#print(puz[i,j,k])
				if puz[i,j,k] == 1:
					tracker += 1
					sol[i,j] = k+1
	print(tracker)
	return sol
	#else:
	#	print('Oh shit')
	#	sol = np.zeros([9,9,9])
	#	for i in range(9):
	#		for j in range(9):
	#			if puz[i,j] != 0:
	#				sol[i,j,puz[i,j]-1]=1
	#	return sol
'''