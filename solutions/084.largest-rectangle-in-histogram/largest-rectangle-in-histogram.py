class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights.append(-1)
        max_area = 0
        index = 0
        for i, height in enumerate(heights):
            if not stack or heights[stack[-1]] <= height:
                stack.append(i)
            else:
                while stack and height < heights[stack[-1]]:         # do while is better
                    top = stack.pop()
                    l = (i - stack[-1] - 1) if stack else i
                    this_area = heights[top] * l
                    
                    max_area = max(this_area, max_area)
                stack.append(i)
        return max_area
        
        