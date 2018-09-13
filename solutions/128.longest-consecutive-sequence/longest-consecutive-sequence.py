class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            d[num] = True
        longest = 0   
        for num in nums:
            if d.get(num):
                d[num] = False
                this_long = 1
                _next, pre = num+1, num-1
                while(d.get(_next)):
                    this_long += 1
                    d[_next] = False
                    _next += 1
                while(d.get(pre)):
                    this_long += 1
                    d[pre] = False
                    pre -= 1
                longest = max(this_long, longest)
            
        return longest
                
        