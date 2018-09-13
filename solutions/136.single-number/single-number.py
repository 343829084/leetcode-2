class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor
        
        # s = set()
        # for num in nums:
        #     if num in s:
        #         s.remove(num)
        #     else:
        #         s.add(num)
        # return s.pop()