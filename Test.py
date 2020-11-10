import numpy as np
import Sudoku as sdk
import matplotlib.pyplot as plt
from Backtracking import Backtracking # wonder if I can just do this or if I have to import whole thing
from Convex import Convex
from time import time

#Aconst = sdk.Make_Aconst()
Aconst = np.load('testFile.npy')
def Run_Simulation(solver,perIn,high,low):
	successRate = np.zeros(high-low)
	timeAvg = np.zeros(high-low)
	timeMax = np.zeros(high-low)
	for i in range(low,high):
		succInter = np.zeros(perIn)
		timeInter = np.zeros(perIn)#list loop here
		print(i)
		for j in range(perIn):
			puzzle = sdk.Make_Puzzle(i)
			t = time()
			solu = eval(solver+'(puzzle)')
			times = time() - t
			if sdk.Check_Puzzle(solu):
				succInter[j] = 1
				timeInter[j] = times

		successRate[i-low] = np.average(succInter) 
		timeInter = timeInter[timeInter != 0]
		if not list(timeInter):
			timeInter = [0]
		else:
			timeAvg[i-low] = np.mean(timeInter)
		timeMax[i-low] = np.max(timeInter)
	return successRate, timeAvg, timeMax
'''
for i in range(10):
	a = sdk.Make_Puzzle(60)
	b = Convex(a)
	isTrue = sdk.Check_Puzzle(b)
	print(isTrue)
#print(b)
#print(a==b)


'''
start = 80; stop = 17; iters = 100;
[convRate,convAvg,convMax] = Run_Simulation('Convex',iters,start,stop)
np.save('convRate100',convRate); np.save('convAvg100',convAvg); np.save('convMax100',convMax);

[backRate,backAvg,backMax] = Run_Simulation('Backtracking',iters,start,stop)
np.save('backRate100',backRate); np.save('backAvg100',backAvg); np.save('backMax100',backMax)

#plt.plot(convMax)
#plt.plot(backMax)
#plt.ylabel('Time (s)')
#plt.xlabel('Initial Points')
#plt.show()


x = list(range(stop,start))
plt.plot(x,backAvg, label = 'Backtracking'); 
plt.plot(x,convAvg, label = 'L-1 Minimization');
plt.legend(); plt.title('Time Average'); plt.show();

plt.plot(x,backMax, label = 'Backtracking'); 
plt.plot(x,convMax, label = 'L-1 Minimization');
plt.legend(); plt.title('Time Max'); plt.show();

plt.plot(x,backRate,label = 'Backtracking')
plt.plot(x,convRate,label = 'L1 Minimization')
plt.title('Success Rate'); plt.legend();
#plt.ax.set_xlim(start,stop); plt.set_ylim(0,1)
plt.show(); 
