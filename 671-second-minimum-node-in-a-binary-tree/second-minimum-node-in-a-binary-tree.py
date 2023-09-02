# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        twoSmallestVals = self.findTwoSmallestVals(root)
        if len(twoSmallestVals) < 2:
            return -1
        return twoSmallestVals[1]


    def findTwoSmallestVals(self, root: Optional[TreeNode]):
        if not root:
            return []
        # return 2 smallest vals

        leftResult = self.findTwoSmallestVals(root.left)
        rightResult = self.findTwoSmallestVals(root.right)

        # everything from left and right result
        candidates = leftResult + rightResult + [root.val]
        candidates = list(set(candidates))
        candidates.sort()

        return candidates[0:2]