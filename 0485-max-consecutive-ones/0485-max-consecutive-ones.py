class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        maxcnt=0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                cnt=0
            maxcnt=max(maxcnt,cnt)
        return maxcnt
            