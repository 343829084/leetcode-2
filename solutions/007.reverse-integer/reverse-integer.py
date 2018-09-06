class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_x = 0
        sign = 1 if x > 0 else -1
        x = x if x > 0 else 0 - x
        while x:
            tmp = x % 10
            x = x / 10
            new_x = 10 * new_x + tmp
            
        return 0 if new_x > math.pow(2, 31) else new_x * sign
       
        