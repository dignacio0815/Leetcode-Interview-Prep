# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        allVals = sorted(set(self.findAllValues(root)))
        if len(allVals) < 2:
            return -1
        # allVals.sort()
        return allVals[1]

    def findAllValues(self, root: Optional[TreeNode]):
        if not root:
            return []
        # return 2 smallest vals

        leftResult = self.findAllValues(root.left)
        rightResult = self.findAllValues(root.right)

        # everything from left and right result
        return leftResult + rightResult + [root.val]
        # candidates = list(set(candidates))
        # candidates.sort()

        # return candidates[0:2]