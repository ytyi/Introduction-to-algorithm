



'''
def mergeSort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    lSort = mergeSort(left)
    rSort = mergeSort(right)

    return merge(lSort, rSort)


def merge(left, right):
    global times
    res = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            times = times + len(left)
            res.append(right.pop(0))
    res += left
    res += right
    return res
'''
def mergesort(L1,L2):
    L=[]
    count=0
    i,j=0,0
    
    while i<len(L1) and j<len(L2):
            if L1[i]<L2[j]:
                
                L.append(L1[i])
                i=i+1
            else:
                count=count+len(L1)-i
                L.append(L2[j])
                
                j=j+1
    
    
    if i>=len(L1):
        while j<len(L2):
            L.append(L2[j])
            
            j=j+1
    if j>=len(L2):
        while i<len(L1):
            L.append(L1[i])
            
            i=i+1
    return count,L




def sort(L):
    left=L[:len(L)//2]
    right=L[len(L)//2:]
    if len(L)==1:
        return 0,L
    else:
        count1,L1=sort(left)
        count2,L2=sort(right)
        count,L=mergesort(L1,L2)
    count=count+count1+count2
    return count,L
    

if __name__ == '__main__':
    count=0
    L = list(map(int, input().split()))
    
    count,L=sort(L)
    print(count)
    print(L)