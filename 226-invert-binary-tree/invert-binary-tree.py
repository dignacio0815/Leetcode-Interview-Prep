# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        tempRoot = root.left
        root.left = root.right
        root.right = tempRoot

        leftResult = self.invertTree(root.left)
        rightResult = self.invertTree(root.right)

        return root