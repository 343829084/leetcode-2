class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = []
        
        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                pre = result[i-1]
                this = [1]
                for index, val in enumerate(pre):
                    if index == len(pre)-1:
                        this.append(val)
                    else:
                        this.append(val+pre[index+1])
                result.append(this)
        return result
        