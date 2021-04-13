import numpy as np
from probability import *
from probability import  South as c 
def findSouth(mat , arrow , state , health ,a,actions , r):
    #print(u)

    if state==1:
        l = np.array([0.0]*600)
        l[index(4,mat,arrow,1,health)] -=c.pMove*(1-c.pAttack)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(1-c.pAttack)
        l[index(4,mat,arrow,0,health)] -=c.pMove*(c.pAttack)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(c.pAttack)
        l[index(4,mat,arrow,state,health)] += 1.0
        a.append(l)
        rewardMilega = -10.0 
        r.append(rewardMilega)
        r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        actions.append('Stay')
        actions.append('Up')
        # actions.append('Up')
        # actions.append['Down']

        l = np.array([0.0]*600)
        l[index(0,mat,arrow,1,health)] -=c.pMove*(1-c.pAttack)
        l[index(1,mat,arrow,1,health)] -= (1-c.pMove)*(1-c.pAttack)
        l[index(0,mat,arrow,0,health)] -=c.pMove*(c.pAttack)
        l[index(1,mat,arrow,0,health)] -= (1-c.pMove)*(c.pAttack)
        l[index(4,mat,arrow,state,health)] += 1.0
        a.append(l)

        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>=0:
            l = np.array([0.0]*600)
            l[index(4,min(mat+1,2),arrow,1,health)] -=c.pGainMat*(1-c.pAttack)
            l[index(4,mat,arrow,1,health)] -=(1-c.pGainMat)*(1-c.pAttack)
            l[index(4,min(mat+1,2),arrow,0,health)] -=c.pGainMat*(c.pAttack)
            l[index(4,mat,arrow,0,health)] -=(1-c.pGainMat)*(c.pAttack)
            l[index(4,mat,arrow,state,health)] += 1.0
            a.append(l)
            r.append(rewardMilega)
            actions.append('Gather')
        if health==2:
            reward = c.profit

    else:
        rewardMilega = -10.0
        r.append(rewardMilega)
        r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        actions.append('Stay')

        actions.append('Up')
        # actions.append('Up')
        # actions.append['Down']
        l = np.array([0.0]*600)
        l[index(4,mat,arrow,1,health)] -=c.pMove*(c.pReady)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(c.pReady)
        l[index(4,mat,arrow,0,health)] -=c.pMove*(1-c.pReady)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(1-c.pReady)
        l[index(4,mat,arrow,state,health)] += 1.0
        a.append(l)


        l = np.array([0.0]*600)
        l[index(0,mat,arrow,1,health)] -=c.pMove*(c.pReady)
        l[index(1,mat,arrow,1,health)] -= (1-c.pMove)*(c.pReady)
        l[index(0,mat,arrow,0,health)] -=c.pMove*(1-c.pReady)
        l[index(1,mat,arrow,0,health)] -= (1-c.pMove)*(1-c.pReady)
        l[index(4,mat,arrow,state,health)] += 1.0
        a.append(l)



        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>=0:

            l = np.array([0.0]*600)
            l[index(4,min(mat+1,2),arrow,1,health)] -=c.pGainMat*(c.pReady)
            l[index(4,mat,arrow,1,health)] -=(1-c.pGainMat)*(c.pReady)
            l[index(4,min(mat+1,2),arrow,0,health)] -=c.pGainMat*(1-c.pReady)
            l[index(4,mat,arrow,0,health)] -=(1-c.pGainMat)*(1-c.pReady)
            l[index(4,mat,arrow,state,health)] += 1.0
            a.append(l)
            r.append(rewardMilega)
            actions.append('Gather')


    return a , actions , r


