def gale(man,woman,mideal,wideal,pair):
    while(1):
        for i in range(0,pair):
            if man[i]==-1:
                for j in range(0,pair):
                    windex=manideal[i][j]
                    if woman[windex]==-2:
                        woman[windex]=i
                        man[i]=windex
                        break
                    else:
                        phindex=woman[windex]
                        for k in range(0,pair):
                            if phindex==womanideal[windex][k]:
                                if i in womanideal[windex][:k]:
                                    woman[windex]=i
                                    man[i]=windex
                                    man[phindex]=-1
                                    break
                        if man[i]!=-1: 
                            break
        pan=1
        for i in range(0,pair):
            if man[i]==-1:
                pan=0
        if pan==1:
            break
            
    
    return man,woman                           
    







if __name__ == '__main__':
    pair = int(input().strip())
    manideal = []
    womanideal = []
    man=[]
    woman=[]
    for i in range(0, pair):
        L = list(map(int, input().strip().split()))
        manideal.append(L)
    input()
    for i in range(0, pair):
        womanideal.append(list(map(int, input().split())))
    for i in range(0,pair):
        man.append(-1)
        woman.append(-2)
    man,woman = gale(man,woman,manideal, womanideal, pair)
    nman,nwoman=gale(man,woman,manideal,womanideal,pair)
    while man!=nman or nwoman!=woman:
        man,woman=nman,nwoman  
        nman,nwoman=gale(man,woman,manideal,womanideal,pair)
    result=[]
    for i in range(0,pair):
        result.append([i,man[i]])
    print(result)
    
