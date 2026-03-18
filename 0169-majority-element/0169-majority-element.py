class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        element=None
        cnt=0
        for i in range(n):
            if cnt==0:
                cnt=1
                element=nums[i]
            elif nums[i]==element:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in range(n):
            if nums[i]==element:
                cnt1+=1
        if cnt1>(n/2):
            return element
        return -1