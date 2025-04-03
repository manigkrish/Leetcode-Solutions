class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if x is None or len(x) <= 3:
            return False

        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i >= 4 and x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                return True
            if i >= 5:
                if (x[i-2] >= x[i-4] and
                    x[i-1] <= x[i-3] and
                    x[i] + x[i-4] >= x[i-2] and
                    x[i-1] + x[i-5] >= x[i-3]):
                    return True

        return False