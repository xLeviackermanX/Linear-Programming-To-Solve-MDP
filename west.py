import numpy as np
from probability import *
from probability import  West as c 
def findWest(mat , arrow , state , health ,a,actions , r):
    #print(u)

    if state==1:
        l = np.array([0.0]*600)
        l[index(2,mat,arrow,1,health)] -=c.pMove*(1-c.pAttack)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(1-c.pAttack)
        l[index(2,mat,arrow,0,health)] -=c.pMove*(c.pAttack)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(c.pAttack)
        l[index(2,mat,arrow,state,health)] += 1.0
        a.append(l)
        rewardMilega = -10.0 
        r.append(rewardMilega)
        r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        actions.append('Stay')
        actions.append('Right')
        # actions.append['Up']
        # actions.append['Down']

        l = np.array([0.0]*600)
        l[index(0,mat,arrow,1,health)] -=c.pMove*(1-c.pAttack)
        l[index(1,mat,arrow,1,health)] -= (1-c.pMove)*(1-c.pAttack)
        l[index(0,mat,arrow,0,health)] -=c.pMove*(c.pAttack)
        l[index(1,mat,arrow,0,health)] -= (1-c.pMove)*(c.pAttack)
        l[index(2,mat,arrow,state,health)] += 1.0
        a.append(l)

        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:
            l = np.array([0.0]*600)
            l[index(2,mat,arrow-1,1,max(health+shootDamage,0))] -=c.pShoot*(1-c.pAttack)
            l[index(2,mat,arrow-1,1,health)] -=(1-c.pShoot)*(1-c.pAttack)
            l[index(2,mat,arrow-1,0,max(health+shootDamage,0))] -=c.pShoot*(c.pAttack)
            l[index(2,mat,arrow-1,0,health)] -=(1-c.pShoot)*(c.pAttack)
            l[index(2,mat,arrow,state,health)] += 1.0
            a.append(l)
            r.append(rewardMilega)
            actions.append('Shoot')
        if health==2:
            reward = c.profit

    else:
        rewardMilega = -10.0
        r.append(rewardMilega)
        r.append(rewardMilega)
        # r.append(rewardMilega)
        # r.append(rewardMilega)
        actions.append('Stay')

        actions.append('Right')
        # actions.append['Up']
        # actions.append['Down']
        l = np.array([0.0]*600)
        l[index(2,mat,arrow,1,health)] -=c.pMove*(c.pReady)
        l[index(1,mat,arrow,1,health)] -=(1-c.pMove)*(c.pReady)
        l[index(2,mat,arrow,0,health)] -=c.pMove*(1-c.pReady)
        l[index(1,mat,arrow,0,health)] -=(1-c.pMove)*(1-c.pReady)
        l[index(2,mat,arrow,state,health)] += 1.0
        a.append(l)


        l = np.array([0.0]*600)
        l[index(0,mat,arrow,1,health)] -=c.pMove*(c.pReady)
        l[index(1,mat,arrow,1,health)] -= (1-c.pMove)*(c.pReady)
        l[index(0,mat,arrow,0,health)] -=c.pMove*(1-c.pReady)
        l[index(1,mat,arrow,0,health)] -= (1-c.pMove)*(1-c.pReady)
        l[index(2,mat,arrow,state,health)] += 1.0
        a.append(l)



        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:

            l = np.array([0.0]*600)
            l[index(2,mat,arrow-1,1,max(health+shootDamage,0))] -=c.pShoot*(c.pReady)
            l[index(2,mat,arrow-1,1,health)] -=(1-c.pShoot)*(c.pReady)
            l[index(2,mat,arrow-1,0,max(health+shootDamage,0))] -=c.pShoot*(1-c.pReady)
            l[index(2,mat,arrow-1,0,health)] -=(1-c.pShoot)*(1-c.pReady)
            l[index(2,mat,arrow,state,health)] += 1.0
            a.append(l)
            r.append(rewardMilega)
            actions.append('Shoot')


    return a , actions , r


