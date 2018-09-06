class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            else:
                if not stack  or stack.pop() != pair.get(p):
                    return False
        if stack:
            return False
        return True
            
        
        