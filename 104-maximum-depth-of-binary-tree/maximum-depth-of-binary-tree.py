# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.maxDepthWithRecursion(root)
        return self.maxDepthWithRecurionOneLiner(root)

    def maxDepthWithRecursion(self, root: Optional[TreeNode]) -> int:
        if root:
            leftResult = 1 + self.maxDepthWithRecursion(root.left)
            rightResult = 1 + self.maxDepthWithRecursion(root.right)
            return max(leftResult, rightResult)
        else:
            return 0

    def maxDepthWithRecurionOneLiner(self, root: Optional[TreeNode]) -> int:
        return max(1 + self.maxDepthWithRecurionOneLiner(root.left), 1 + self.maxDepthWithRecurionOneLiner(root.right)) if root else 0