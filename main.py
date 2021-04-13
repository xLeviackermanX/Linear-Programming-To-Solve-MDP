import numpy as np
from centre import *
from north import *
from east import *
from west import *
from south import *
from probability import *
import cvxpy as cp
import json

class Tile:
    def __init__(self,a,b,c,d,e):
        self.pos = a
        self.mat = b
        self.arrow = c
        self.state = d
        self.health = e
        self.actions = []

    def convert(self):
        self.actions = np.array(self.actions)

tiles = []
r = []
a = []
start = 0
for pos in range(0,5):
    for mat in range(0,3):
        for arrow in range(0,4):
            for state in range(0,2):
                for health in range(0,5):
                    if pos==0 and mat==1 and arrow==1 and state==1 and health==1:
                        start = len(r)
                    x= Tile(pos,mat,arrow,state,health)
                    tiles.append(x)
                    if health==0:
                        l = np.array([0.0]*600)
                        l[index(pos,mat,arrow,state,health)] = 1.0
                        a.append(l)
                        x.actions.append('None')
                        r.append(0)
                    elif pos==0:
                        a , x.actions ,r = findCentre(mat , arrow , state , health,a,x.actions,r)
                    elif pos==1:
                        a , x.actions ,r = findEast(mat , arrow , state , health,a,x.actions,r)
                    elif pos==2:
                        a , x.actions ,r = findWest(mat , arrow , state , health,a,x.actions,r)
                    elif pos==3:
                        a , x.actions ,r = findNorth(mat , arrow , state , health,a,x.actions,r)
                    elif pos==4:
                        a , x.actions ,r = findSouth(mat , arrow , state , health,a,x.actions,r)
                    x.convert()
tiles = np.array(tiles)
r = np.array(r)
a = np.array(a)

row = len(a)
col = len(a[0])
A = np.array([[0.0]*row]*col)
for i in range(0,col):
    for j in range(0,row):
        A[i][j] = a[j][i]

alpha = np.array([[0.0]*1]*600)
alpha[index(0,2,3,1,4)][0] = 1.0
alphaMain = np.array([0.0]*600)
alphaMain[index(0,2,3,1,4)] = 1.0
k1 = len(r)
R = np.array([[0.0]*k1]*1)
for i in range(0,k1):
    R[0][i] = r[i]
X = cp.Variable(shape=(k1,1), name="X")
constraints = [cp.matmul(A, X) == alpha, X>=0]
objective = cp.Maximize(cp.matmul(R, X))
problem = cp.Problem(objective, constraints)
solution = problem.solve()
print(solution)
# print(a[1])
Y = list(X.value)
Ym = [ float(val) for val in Y]
ind =0
bestAction = []
for pos in range(0,5):
    for mat in range(0,3):
        for arrow in range(0,4):
            for state in range(0,2):
                for health in range(0,5):
                    x = tiles[index(pos,mat,arrow,state,health)]
                    tup = (position[pos],mat,arrow,stateName[state],health*25)

                    p = []
                    p.append(tup)
                    be = 'None'
                    maxi = -1e18
                    for i in range(0,len(x.actions)):
                        if maxi<=Ym[ind+i]:
                            be = x.actions[i]
                            maxi = Ym[ind+i]
                    ind+=len(x.actions)
                    p.append(be.upper())
                    bestAction.append(p)


diction = {"a":A.tolist() , "r":r.tolist(),"alpha":alphaMain.tolist(),"x":Ym,"policy":bestAction,"objective":solution}

json_object = json.dumps(diction, indent=4)

with open("./outputs/part_3_output.json","w") as writeFile:
    writeFile.write(json_object)
print(k1)
