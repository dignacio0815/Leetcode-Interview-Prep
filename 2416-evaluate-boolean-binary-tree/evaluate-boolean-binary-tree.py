# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.recursion(root)
        # return self.shortCiruit(root)


    def shortCiruit(self, root: Optional[TreeNode]) -> bool:
        if root is None or (0 <= root.val <= 1):
            return root is not None and root.val == 1
        
        leftResult = self.shortCiruit(root.left)

        if(root.val == 2 and leftResult) or (root.val == 3 and not leftResult):
            return leftResult

        return self.shortCiruit(root.right)

    def recursion(self, root: Optional[TreeNode]) -> bool:
        # base cases lines 10 - 11
        if root is None or 0 <= root.val <= 1:
            return root is not None and root.val == 1
        
        # compute child results
        leftResult = self.evaluateTree(root.left)
        rightResult = self.evaluateTree(root.right)

        # assemble child results for our current node
        return (leftResult and rightResult) if root.val == 3 else (leftResult or rightResult)