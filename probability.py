import numpy as np

gamma = 0.25
delta  = 0.001
score = 0
stateName = np.array(['D','R'])
actionIndex = {'Stay':0, 'Right':1,'Left':2,'Up':3,'Down':4,'Shoot':5,'Hit':6,'Gather':7,'Craft':8,'None':9}
actionAll  = np.array(['Stay' , 'Right', 'Left', 'Up','Down','Shoot','Hit','Gather','Craft','None'])
position = np.array(['C','E','W','N','S'])
healthMultiple = 25.0
stepCost = -10.0
def index(a,b,c,d,e):
    i = int(120*a+40*b+10*c+5*d+e)
    return i

def writeFile(s):
    out = open("trace.txt","a")
    out.write(s+'\n')
    out.close()
shootDamage = -1

class Common:
    bladeDamage = -2
    pReady = 0.2
    pAttack = 0.5
    healthRegain = +1
    loss = -40.0
    profit = +50.0

class Centre(Common):
    pMove = 0.85
    pShoot = 0.5
    pBlade = 0.1
    pAction = 1/7

class East(Common):
    pMove = 1.0 
    pShoot = 0.9
    pBlade = 0.2
    pAction = 1/4

class West(Common):
    pMove = 1.0
    pShoot = 0.25

class North(Common):
    pMove = 0.85
    pOneArrow = 0.5
    pTwoArrow = 0.35
    pThreeArrow = 0.15

class South(Common):
    pMove = 0.85
    pGainMat = 0.75
