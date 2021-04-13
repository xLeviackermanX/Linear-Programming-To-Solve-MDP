import numpy as np
from probability import *
from probability import  North as c 
def findNorth(mat , arrow , state , health ,a,actions , r):
    #print(u)

    if state==1:
        l = np.array([0.0]*600)
        l[index(3,mat,arrow,1,health)] -=c.pMove*(1-c.pAttack)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(1-c.pAttack)
        l[index(3,mat,arrow,0,health)] -=c.pMove*(c.pAttack)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(c.pAttack)
        l[index(3,mat,arrow,state,health)] += 1.0
        a.append(l)
        rewardMilega = -10.0 
        r.append(rewardMilega)
        r.append(rewardMilega)

        # r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        actions.append('Stay')
        actions.append('Down')
        # actions.append['Up']
        # actions.append('Down')

        l = np.array([0.0]*600)
        l[index(0,mat,arrow,1,health)] -=c.pMove*(1-c.pAttack)
        l[index(1,mat,arrow,1,health)] -= (1-c.pMove)*(1-c.pAttack)
        l[index(0,mat,arrow,0,health)] -=c.pMove*(c.pAttack)
        l[index(1,mat,arrow,0,health)] -= (1-c.pMove)*(c.pAttack)
        l[index(3,mat,arrow,state,health)] += 1.0
        a.append(l)

        reward = 0.0
        if health<2:
            reward = c.profit
        if mat>0:
            l = np.array([0.0]*600)
            l[index(3,mat-1,min(arrow+1,3),1,health)] -=c.pOneArrow*(1-c.pAttack)
            l[index(3,mat-1,min(arrow+1,3),0,health)] -=c.pOneArrow*(c.pAttack)
            l[index(3,mat-1,min(arrow+2,3),1,health)] -=c.pTwoArrow*(1-c.pAttack)
            l[index(3,mat-1,min(arrow+2,3),0,health)] -=c.pTwoArrow*(c.pAttack)
            l[index(3,mat-1,min(arrow+3,3),1,health)] -=c.pThreeArrow*(1-c.pAttack)
            l[index(3,mat-1,min(arrow+3,3),0,health)] -=c.pThreeArrow*(c.pAttack)
            l[index(3,mat,arrow,state,health)] += 1.0
            a.append(l)
            r.append(rewardMilega)
            actions.append('Craft')
        if health==2:
            reward = c.profit

    else:
        rewardMilega = -10.0
        r.append(rewardMilega)
        r.append(rewardMilega)
        l = np.array([0.0]*600)
        l[index(3,mat,arrow,1,health)] -=c.pMove*(c.pReady)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(c.pReady)
        l[index(3,mat,arrow,0,health)] -=c.pMove*(1-c.pReady)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(1-c.pReady)
        l[index(3,mat,arrow,state,health)] += 1.0
        a.append(l)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        actions.append('Stay')

        actions.append('Down')
        # actions.append['Up']
        # actions.append('Down')
        l = np.array([0.0]*600)
        l[index(0,mat,arrow,1,health)] -=c.pMove*(c.pReady)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(c.pReady)
        l[index(0,mat,arrow,0,health)] -=c.pMove*(1-c.pReady)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(1-c.pReady)
        l[index(3,mat,arrow,state,health)] += 1.0
        a.append(l)

        if mat>0:
            l = np.array([0.0]*600)
            l[index(3,mat-1,min(arrow+1,3),1,health)] -=c.pOneArrow*(c.pReady)
            l[index(3,mat-1,min(arrow+1,3),0,health)] -=c.pOneArrow*(1-c.pReady)
            l[index(3,mat-1,min(arrow+2,3),1,health)] -=c.pTwoArrow*(c.pReady)
            l[index(3,mat-1,min(arrow+2,3),0,health)] -=c.pTwoArrow*(1-c.pReady)
            l[index(3,mat-1,min(arrow+3,3),1,health)] -=c.pThreeArrow*(c.pReady)
            l[index(3,mat-1,min(arrow+3,3),0,health)] -=c.pThreeArrow*(1-c.pReady)
            l[index(3,mat,arrow,state,health)] += 1.0       
            a.append(l)
            r.append(rewardMilega)
            actions.append('Craft')



    return a , actions , r


