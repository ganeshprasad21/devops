def print_until_n(n,i=0):
    if i == n+1:
        return
    if i%2 == 0:
        print(i)  #head
    print_until_n(n,i+1)
    # print(i)  #tail


print_until_n(6)

#tree
## bst
# it is a non linear data structure

# there is root node andf the remaining nodes are partitioned into trees known as subtrees
"""
BST
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root: Node,val):
    if root == None:
        root = Node(val)
        return root
    if val > root.val:
        root.right = insert(root.right,val)
    elif val < root.val :
        root.left = insert(root.left,val)
    return root

root = None
root = insert(root, 8)
insert(root, 3)
insert(root, 10)
insert(root, 1)
insert(root, 6)
insert(root, 14)
insert(root, 4)
insert(root, 7)
insert(root, 13)
print(root.val, root.right.val, root.left.val)

def search(root: Node,val):
    if root is None or root.val == val:
        return root
    if root.val > val:
        search()
