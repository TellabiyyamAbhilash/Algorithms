#### SELECTION SORT###


#     0   1   2    3   4   5
#     5   15  3   12  17   0

# select the min element in the list using comparision
# first we compare the 0th index and 1st index and hold the min value as "min_val" and comapre than vaue to tha remaining 
# to the last index of the list and get the min_value in the list and swap it with the minindex which is 0th while at the
# first check

#After first check the list will become 

#     0  | 1   2    3   4   5
#     0  | 15  3   12  17   5

# 0th index is the sorted and the remaining from the 1st index is unsorted 

#now repeat the same process with remaining list from 1st index to last

#After 2nd check

#     0   1  | 2    3   4   5
#     0   3  | 15   12  17   5

#After 3rd check

#     0   1   2  |  3   4   5
#     0   3   5  | 12  17   15

#After 4th check

#     0   1   2    3  | 4   5
#     0   3   5   12  |17   15

#After 5th check

#     0   1   2    3   4  | 5
#     0   3   5   12  15  |17


list = [5,15,3,12,17,0]
print("unsorted list:",list)
for i in range(len(list)-1):
    min_value=list[i]
    min_ind = i
    for j in range(i+1,len(list)):
        if list[j]<min_value:
            min_value=list[j]
            min_ind = j
    list[i],list[min_ind]=list[min_ind],list[i]
    print(list)
print("sorted list :",list)




