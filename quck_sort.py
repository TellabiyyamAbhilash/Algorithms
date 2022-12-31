### Quick Sort

# we have to selct a pivot first which is mostly the last element in general case
# so now lets take the first element index as l and r as the pivot element preceding element index

#for l
#make i=l
#check the ith element is lessthan the pivot or not if yes increment it by 1
#and it should also be that the index has to be less than the r

#for r
# make j=r-1
#check if the jth element is greater than or equal to the pivot element if yes decrement by 1
#and the index should also be greater then the l

#if the i<j swap the itha and jth element

#after this if the ith element is greater then the pivot eleemnt swap them
# and return the index i for next partition


def quicksort(list,l,r):
    if l<r:
        pos=partition(list,l,r)
        quicksort(list,l,pos-1)
        quicksort(list,pos+1,r)

def partition(list,l,r):
    i=l
    j=r-1
    while i<j:
        while i<r and list[i]<list[r]: 
            i+=1
        while j>l and list[j]>=list[r]:
            j-=1
        if i<j:
            list[i],list[j]=list[j],list[i]
    if list[i]>list[r]:
        list[i],list[r]=list[r],list[i]
    return i
    
list = [22,11,88,66,55,77,33,44]
quicksort(list,0,len(list)-1)
print(list)


