#求最大的连续的子序列的和
def maxContinueSum(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    ret = dp[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        ret = max(ret, dp[i])
    print(dp)
    return ret

nums = [-1, -2, 1, 2,3, -1, 1]
print(maxContinueSum(nums))


