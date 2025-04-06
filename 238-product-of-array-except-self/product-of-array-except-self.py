class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix  = [1] * len(nums)
        postfix = [1] * len(nums)
        output  = [1] * len(nums)

        # calculate prefixes
        preProduct = 1
        postProduct = 1
        for i in range(len(nums)):
            preProduct *= nums[i]
            prefix[i] = preProduct
            
            postProduct *= nums[len(nums) - i - 1]            
            postfix[len(nums) - i - 1] = postProduct
        print(postfix)

        for i in range(len(nums)):
            left  = prefix[i-1] if i - 1 >= 0 else 1
            right = postfix[i+1] if i + 1 < len(nums) else 1
            output[i] = left * right

        return output
"""
create prefix and postfix product array 

loop through nums and basically just take the index - 1 * index + 1 and that's the current product except self

i.e. nums = [1,2,3,4]
prefix    = [1,2,6,24]
postfix   = [24,24,12,4]

in the event i-1 or i+1 is OoB, than assume it multiplies by 1
"""