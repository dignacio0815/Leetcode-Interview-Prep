# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # base cases lines 10 - 14
        if root.val == 1:
            return True

        if root.val == 0:
            return False
        
        # compute child results
        leftResult = self.evaluateTree(root.left)
        rightResult = self.evaluateTree(root.right)

        # assemble child results for our current node
        if root.val == 3:
            return leftResult and rightResult

        if root.val == 2:
            return leftResult or rightResult
