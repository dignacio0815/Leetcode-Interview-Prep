# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # base cases lines 10 - 11
        if root is None or 0 <= root.val <= 1:
            return root is not None and root.val == 1
        
        # compute child results
        leftResult = self.evaluateTree(root.left)
        rightResult = self.evaluateTree(root.right)

        # assemble child results for our current node
        return (leftResult and rightResult) if root.val == 3 else (leftResult or rightResult)