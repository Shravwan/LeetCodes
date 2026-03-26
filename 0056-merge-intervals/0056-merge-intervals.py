class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans=[]
        n=len(intervals)
        for i in range(n):
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans