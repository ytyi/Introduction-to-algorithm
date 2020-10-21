import timeit
import numpy as np
import random
import matplotlib.pyplot as plt

def knapsack(total,L):
    
    if total==0:
        return 1,[]
    if len(L)==1 and L[0]!=total:
        return 0,[]
    elif len(L)==1 and L[0]==total:
        return 1,L
    else:
        num=L[0]
        Lti=[]
        for i in range(0,len(L)):
            Lti.append(L[i])
        Lti.pop(0)
        if(num>total):
            return knapsack(total,Lti)
        else:
            flag1,L1=knapsack(total,Lti)
            if flag1==1:
                return 1,L1
            else:
                flag2,L2=knapsack(total-num,Lti)
                if flag2==1:
                    L2.insert(0,num)
                    return 1,L2
                else:
                    return 0,[]

def knapsack_big(total,L):
    L.sort(reverse=True)
    if total==0:
        return 1,[]
    if len(L)==1 and L[0]!=total:
        return 0,[]
    elif len(L)==1 and L[0]==total:
        return 1,L
    else:
        num=L[0]
        Lti=[]
        Lres=[]
        for i in range(0,len(L)):
            Lti.append(L[i])
        Lti.pop(0)
        if num>total:
            return 0,[]
        else:
            index,Lres=knapsack_big(total-num,Lti)
            if index==0:
                return 0,[]
            else:
                Lres.insert(0,num)
                return 1,Lres

def knapsack_small(total,L):
    L.sort()
    if total==0:
        return 1,[]
    if len(L)==1 and L[0]!=total:
        return 0,[]
    elif len(L)==1 and L[0]==total:
        return 1,L
    else:
        num=L[0]
        Lti=[]
        Lres=[]
        for i in range(0,len(L)):
            Lti.append(L[i])
        Lti.pop(0)
        if num>total:
            return 0,[]
        else:
            index,Lres=knapsack_small(total-num,Lti)
            if index==0:
                return 0,[]
            else:
                Lres.insert(0,num)
                return 1,Lres
        
            
        

        










if __name__ == '__main__':
    '''
    total = int(input().strip())
    L = list(map(int, input().strip().split()))
    
    index,Lres = knapsack_small(total,L)
    Lres.sort()
    if total!=0 and Lres==[]:
        print()
    else:
        print(Lres)
    '''
    timetrue = []
timesmall = []
timebig = []
input()
for i in range(50):
    print(i+1,"%")
    b=range(0,i,1)
    S=random.sample(b,i)
    n = int(sum(S)/2)
    timetrue.append(timeit.timeit("knapsack(n,S)","from __main__ import knapsack,n,S",number=50))
    timesmall.append(timeit.timeit("knapsack_small(n,S)","from __main__ import knapsack_small,n,S",number=1000))
    timebig.append(timeit.timeit("knapsack_big(n,S)","from __main__ import knapsack_big,n,S",number=1000))

plt.figure(1)
plt.plot(np.linspace(0,49,50),np.array(timetrue),label="Correct Algorithm",ls='--')
plt.plot(np.linspace(0,49,50),np.array(timesmall),label="knap_small Algorithm")
plt.plot(np.linspace(0,49,50),np.array(timebig),label="knap_big Algorithm",ls='-.')
plt.xlabel("Size of the input permutation n")
plt.ylabel("time(s)")
plt.legend()
plt.show()