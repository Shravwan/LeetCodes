class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def nCr(n,r):
            res=1
            for i in range(r):
                res*=(n-i)
                res//=(i+1)
            return res
        result=[]
        for i in range(1,numRows+1):
            temp=[]
            for j in range(1,i+1):
                temp.append(nCr(i-1,j-1))
            result.append(temp)
        return result