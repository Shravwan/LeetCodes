class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=0
        maxSum=-(float('inf'))
        n=len(nums)
        for i in range(n):
            curSum+=nums[i]
            maxSum=max(maxSum,curSum)
            if curSum<0:
                curSum=0
        return maxSum