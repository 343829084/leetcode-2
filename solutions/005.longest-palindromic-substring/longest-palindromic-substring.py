class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        max_len, start = 0, 0
        dp = [[False]*size for x in range(size)]
        for i in range(size):
            for j in range(i+1):
                if s[j] == s[i] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if (i-j+1)>max_len:
                        max_len, start = i-j+1, j
        return s[start:start+max_len]
                        
        