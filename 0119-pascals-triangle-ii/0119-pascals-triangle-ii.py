class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]

        pre = [1]  

        for i in range(1, rowIndex + 1):
            curr = [1]  
            for j in range(len(pre) - 1):
                curr.append(pre[j] + pre[j + 1])
            curr.append(1) 
            pre = curr  

        return pre
