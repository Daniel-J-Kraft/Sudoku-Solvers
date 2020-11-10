import Sudoku as sdk
import numpy as np
from scipy.optimize import linprog
from cvxopt import matrix, solvers
import seaborn as sns

Aconst = sdk.Make_Aconst()

def Convert_Initial(puz):
    Aclue = np.zeros([np.count_nonzero(puz),729])
    clueNum = 0
    for i in range(9):
        for j in range(9):
            if puz[i,j] != 0:
                Aclue[clueNum, int(81*i+9*j+puz[i,j])-1] = 1
                clueNum += 1
    return Aclue

def Convex(puz):    
    Ahint = Convert_Initial(puz)
    A = np.vstack([Ahint,Aconst])
    onesA = np.ones([np.shape(A)[1],1])
    onesB = np.ones([np.shape(A)[0],1])
    res = linprog(onesA, A_eq=A, b_eq=onesB)
    sol = sdk.Convert_Puzzle(res['x'])
    
    #resSim = linprog(onesA, A_eq = A, b_eq = onesB,method = 'revised simplex')
    #h = matrix(np.zeros([729,1]),(729,1),'d'); A = matrix(A,np.shape(A),'d'); b = matrix(onesB,np.shape(onesB),'d');
    #G = matrix(-np.eye(729)); c = matrix(onesA, np.shape(onesA),'d')
    #res = solvers.lp(c=c, A=A, b=b, G=G, h=h,kktsolver='ldl', options={'kktreg':1e-9})
    
    #print(np.shape(Acheck))
    #print(np.shape(res['x']))
    #print(sum(res['x']))
    #print(sum(res['x']).astype(int))
    #Acheck = np.matmul(A,res['x'])#should be all ones
    #print(Acheck)   

    #sdk.Convert_Puzzle(np.reshape(convsol)) #change reshape to do this for you 729x1 b2 to 9x9 b10

    return(sol.astype(int))


