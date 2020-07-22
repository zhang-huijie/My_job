class Solution:
    def twoSum(self,nums,target):
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            if nums[l] +  nums[r] == target:
                return [nums[l],nums[r]]
            elif nums[l] +  nums[r] > target:
                r -= 1
            else:
                l += 1
        return

