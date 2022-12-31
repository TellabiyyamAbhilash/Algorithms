#### insertion_sort

# First select a element and compare it with the left elements and arrange that at the
# correct position

#  0   1   2   3   4
# 10   4  25   1   5


# first iteration

# 10   4   25   1   5
# ^
# 4   10  ||  25   1   5
# sorted      unsorted

# second Iteration
# 4   10   ||   25   1   5
# 25 is greater then all the sorted elements so no changes here 
# and 25 will come under sorted now

# third iteration

# 4   10   25   ||   1   5
#                    ^
# 4   10   1    25   5
#          ^
# 4   1   10    25   5
#     ^
# 1   4   10   25    ||   5

# Fourth Iteration

# 1   4   10   25   ||   5
#                        ^
# 1   4   10   5   25
#              ^
# 1   4   5   10   25
#         ^
# 1   4   5   10   25   ||
# here 5 is greater than the left side elements so it will stop there



list=[2,4,3,5,1]
len=len(list)
print("Unsorted list : ", list)
for i in range(1,len):
    idx=i
    j=i-1
    while j>=0:
        if list[j]>list[idx]:
            list[idx],list[j]=list[j],list[idx]
        print(list)
        idx=j
        j=j-1
    print("\n",list,"\n")
print("sorted list :",list)

        


