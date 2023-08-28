# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchBSTNaive(root, val)
    
    def searchBSTNaive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root equals none or found the node, return it
        if root == None or root.val == val:
            return root
        
        # search both left / right sides of tree
        leftResult = self.searchBSTNaive(root.left, val)
        rightResult = self.searchBSTNaive(root.right, val)

        if leftResult:
            return leftResult

        if rightResult:
            return rightResult