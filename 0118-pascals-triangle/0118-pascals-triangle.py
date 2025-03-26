class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        result = []
        pre = [1]  
        result.append(pre)

        for i in range(1, numRows):
            curr = [1] 
            for j in range(len(pre) - 1):
                curr.append(pre[j] + pre[j + 1])
            curr.append(1)  
            result.append(curr)
            pre = curr  

        return result
