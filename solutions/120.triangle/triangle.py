class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        length = len(triangle)
        
        min_path = [[0] * len(triangle[-1])] * length
        for i in range(length-1,-1,-1):
            for j, num in enumerate(triangle[i]):
                if i == length -1:
                    min_path[i][j] = triangle[i][j]
                else:
                    min_path[i][j] = min(min_path[i+1][j], min_path[i+1][j+1]) + triangle[i][j]
        return min_path[0][0]
        