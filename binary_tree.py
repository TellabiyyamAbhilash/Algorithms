import collections
# DEFINATION AND DEFINING A BINARY TREE #
########################################

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.value=data

    def insert(self,data):
        if self.value is None:
            self.value=data
        else:
            if self.value>data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.value < data:
                    if self.right is None:
                        self.right=Node(data)
                    else:
                        self.right.insert(data)

# INSERTING THE VALUES INTO THE TREE IN MAIN FUNCTION #

# SO TO PRINT THE ALL VALUES IN THE TREE #
# WE HAVE TO USE THE TRAVERSAL TECHNIstackUE #
# WE HAVE THREE TRAVERSAL TECHNIstackUES # 
# 1. INORDER TRAVERSAL #
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# 2. PREORDER TRAVERSAL #
def preorder(root):
    if root is None:
        return
    else:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# 3. POSTORDER TRAVERSAL #
def postorder(root):
    if root is None:
        return
    else:
        postorder(root.left) 
        postorder(root.right)
        print(root.value, end=" ")

# BREADTH FIRST SEARCH #
######################
# searching for a node levelly is caled breadth for search 
# for making this happen we need to have twoo things
# Adjacency List or Adjacency Matrix
# Here is afunction to make a Adjacency list which is a dictionary
def makeAdjList(root):
    if root is None:
        return
    else:
        AdjListDict[root.value] = []
        makeAdjList(root.left)
        if root.left:
            AdjListDict[root.value].append(root.left.value)
        if root.right:
            AdjListDict[root.value].append(root.right.value)
        makeAdjList(root.right)

# BREADTH FIRST SEARCH #
def BFS(AdjListDict,startnode):
    stack = [startnode]
    visited = []
    while stack:
        node = stack.pop(0)###bottom of the stack
        visited.append(node)
        for x in AdjListDict[node]:
            stack.append(x)
    print(visited)

# DEAPTH FIRST SEARCH #
def DFS(AdjListDict,startnode):
    stack=[startnode]
    visited = []
    while stack:
        node = stack.pop() ### top of the stack
        if node not in visited:
            visited.append(node)
        for x in AdjListDict[node]:
            stack.append(x)
    print(visited)




if __name__=='__main__':
    root=Node(7)
    ar=[3,2,1,5,4,6,9,8,10,11]
    for i in ar:
        root.insert(i)
    print(root.value) # PRINTS THE ROOT VALUE BUT NOT THE REMAINING
    print("INORDER")
    inorder(root)
    print("\nPREORDER")
    preorder(root)
    print("\nPOSTORDER")
    postorder(root)
    AdjListDict = {}
    makeAdjList(root)
    print(AdjListDict)
    print("\nBFS TRAVEL")
    BFS(AdjListDict,root.value)
    print("\nDFS TRAVEL")
    DFS(AdjListDict,root.value)
    