class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [0] * (n+1)
        d[0] = d[1] = 1
        for i in range(1, n+1):          # traversal
            this_sum = 0
            for j in range(1, i+1):       # sub_quest
                this_sum += d[j - 1] * d[i - j]
            d[i] = this_sum
        
        return d[n]