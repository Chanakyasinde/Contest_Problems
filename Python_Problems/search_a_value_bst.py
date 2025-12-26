"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
def searchBST(root, x):
    # code here
    lst = []
    inorder(root, lst)
    n = len(lst)
    for i in range(n):
        if lst[i] == x:
            return True
    return False


def inorder(root, lst):
    if root is None:
        return 
    inorder(root.left, lst)
    lst.append(root.val)
    inorder(root.right, lst)
