class Solution(object):
    @staticmethod
    def _get_op(op):
        def div(a, b):
            """something differnt form inbuilt /"""
            sign = 1 if a * b > 0 else -1
            return sign * (abs(a) / abs(b))
        
        d = {
            '+': lambda a, b: a + b, 
            '-': lambda a, b: a - b, 
            '*': lambda a, b: a * b, 
            '/': div
        }
        return d.get(op)
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        result = 0
        for item in tokens:
            if item not in ['+', '-', '*', '/']:  # operand
                stack.append(int(item))
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(self._get_op(item)(o1, o2))
        return stack.pop()
        