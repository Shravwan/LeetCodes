class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                summ=a+nums[l]+nums[r]
                if summ==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif summ<0:
                    l+=1
                else:
                    r-=1
        return res