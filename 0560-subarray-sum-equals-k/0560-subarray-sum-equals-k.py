class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum=0
        mapping=defaultdict(int)
        mapping[0]=1
        cnt=0
        n=len(nums)
        for i in range(n):
            preSum+=nums[i]
            remove=preSum-k
            if remove in mapping:
                cnt+=mapping[remove]
            mapping[preSum]+=1
        return cnt