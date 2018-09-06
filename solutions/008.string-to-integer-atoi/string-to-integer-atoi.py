class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        sign = 1
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        str = str.strip()
        if str and str[0] in ['+', '-']:
            if str[0] == '-':
                sign *= -1
            str = str[1:]
        for c in str:
            if '0' <= c <= '9':
                result = result*10 + int(c)
            else:
                break
        result = result * sign
        if result > INT_MAX:
            result = INT_MAX
        if result < INT_MIN:
            result =INT_MIN
        return result