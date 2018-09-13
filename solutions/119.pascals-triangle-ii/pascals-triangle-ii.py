class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre, this = None, None
        for i in range(rowIndex+1):
            if i == 0:
                pre = this = [1]
            else:
                this = [1]
                for index, val in enumerate(pre):
                    if index == len(pre)-1:
                        this.append(val)
                    else:
                        this.append(val+pre[index+1])
                pre = this
        return this
        

        