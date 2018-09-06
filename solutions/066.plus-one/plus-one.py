class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        to_plus = 1
        for i in range(len(digits)-1,-1,-1):
            plus = digits[i] + to_plus
            digits[i] = plus % 10
            to_plus = plus / 10
            if not to_plus:
                break
        if to_plus:
            digits.insert(0, to_plus)
        return digits