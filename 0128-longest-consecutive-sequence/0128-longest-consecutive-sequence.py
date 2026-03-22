class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set(nums)
        long=0
        for i in num:
            if (i-1) not in num:
                length=1
                while (i+length) in num:
                    length+=1
                long=max(long,length)
        return long