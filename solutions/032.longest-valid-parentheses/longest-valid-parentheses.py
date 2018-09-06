class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_len = 0
        this_max = 0
        last = -1  # last position of unmatched ')'
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)   # append --> push
            elif not stack:
                this_max = 0
                last = i
            else:
                stack.pop()
                if not stack:
                    this_max = i - last
                else:
                    this_max = i - stack[-1]   # -1 --> top
                max_len = max(max_len, this_max)
        return max_len
        