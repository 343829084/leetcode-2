class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        i = 3
        result = 0
        while i <= n:
            result = a + b
            a, b = b, result
            i += 1
        return result
        