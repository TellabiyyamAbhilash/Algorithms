### MERGE SORT

    #                [10    15     4     3      2      0]
    #                         /               \
    #                        /                 \
    #        [10      15      4 ]              [3       2       0]
    #              /          \                   /            \
    #             /            \                 /              \
    #     [10      15]           [4]       [3       2]            [0]                       
    #     /        \                      /       \
    #    /          \                    /         \
    #   [10]         [15]             [3]        [2]

# the list will be divide like this to a single element and 
# will merge them by comapring from down to up

#  #   [10]         [15]             [3]        [2]
#        \            /               \          /
#         \          /                 \        /
#           [10,15]      [4]              [2,3]       [0] 
#             \          /                  \           /
#              \        /                    \         /
#               [4,10,15]                      [0,2,3]
#                   \                            /
#                    \                          / 
#                         [0,2,3,4,10,15]

# this is how we will merge them to make a sorted list


# Function to divide the array


def merge_sort(list):
    if len(list)>1:
        left_list = list[:(len(list))//2]
        right_list = list[len(list)//2:]
        merge_sort(left_list)
        merge_sort(right_list)

        i=0 #left_list indx
        j=0 #right_list indx
        k=0 #list indx

        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list[k]=left_list[i]
                i+=1
            else:
                list[k]=right_list[j]
                j+=1
            k+=1
        while i<len(left_list):
            list[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            list[k]=right_list[j]
            j+=1
            k+=1
        print(list)

list = [10,15,4,3,2,0]
merge_sort(list)
print(list)


# [10, 15, 4]
# [3, 2, 0]

# [10]
# [15, 4]

# [15]
# [4]

# [4, 15]

# [4, 10, 15]

# [3]
# [2, 0]

# [2]
# [0]

# [0, 2]

# [0, 2, 3]

# [0, 2, 3, 4, 10, 15]
# [0, 2, 3, 4, 10, 15]