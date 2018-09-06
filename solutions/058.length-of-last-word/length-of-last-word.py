class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        split_s = s.split()
        return len(split_s[-1]) if split_s else 0
        