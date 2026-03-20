class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        arr=[0]*n
        posidx=0
        negidx=1
        for i in range (n):
            if nums[i]<0:
                arr[negidx]=nums[i]
                negidx+=2
            else:
                arr[posidx]=nums[i]
                posidx+=2
        return arr