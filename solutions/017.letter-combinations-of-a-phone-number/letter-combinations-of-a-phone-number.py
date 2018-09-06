class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        char_list = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        from itertools import product
        for item in product(*[char_list[int(digit)] for digit in digits]):
            cur = ''
            for c in item:
                cur += c
            result.append(cur)
        return result
        
        