# """   BUBBLE SORT     """

# start with first element and compare it with the next element
# if the current element is lessthan the previous then swap them and repeat the first step

#    0    1    2    3    4
#   10    15   4    23   0

# first iteration

#   10    15   4    23   0
#   ^
#   10    4    15   23   0
#         ^
#   10    4    15   23   0
#              ^
#   10    4    15    0   23
#                    ^


# second iteration

#   10    4    15   0   23
#   ^
#   4     10   15   0   23
#         ^
#   4     10   0    15   23
#              ^
#   4     10   0    15   23
#                    ^

# third iteration

#   4     10   0    15   23
#   ^
#   4     0    10   15   23
#         ^
#   4     0    10   15   23
#              ^
#   4     0    10   15   23
#                    ^

# fourth iteration

#   4     0    10    15   23
#   ^
#   0     4    10   15   23
#         ^
#   0     4    10   15   23
#              ^
#   0     4    10   15   23
#                    ^



list1=[10,15,4,23,0]
list2=[10,15,4,23,0]
len=len(list1)
print("unsorted list1 :", list1)

########## ASCENDING

for i in range(len-1):
    for j in range(1,len):
        if list1[j-1]>list1[j]:
            list1[j],list1[j-1]=list1[j-1],list1[j]
        print(list1)
    print("\n",list1,"\n")
print("Ascending sorted list1 :", list1)

########## DESCENDING

for i in range(len-1):
    for j in range(1,len):
        if list2[j-1]<list2[j]:
            list2[j],list2[j-1]=list2[j-1],list2[j]
        print(list2)
    print("\n",list2,"\n")
print("Descending sorted list1 :", list2)