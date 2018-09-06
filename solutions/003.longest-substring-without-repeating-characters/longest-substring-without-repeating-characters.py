class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        _max = 0
        left = 0
        d = {}

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            this_max = i - left + 1
            _max = max(_max, this_max)
        return _max

        