class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str1 = "1"
        for i in range(n-1):
            str1 = self.getNext(str1)
            
        return str1
        
    def getNext(self, str1):
        num_counts = []
        result = ""
        pre_count = 1
        pre_num = str1[0]
        for num in str1[1:]:
            if num == pre_num:
                pre_count += 1
            else:
                num_counts.append((pre_num, pre_count))
                pre_num = num
                pre_count = 1
        else:
            num_counts.append((pre_num, pre_count))
        for num, count in num_counts:
            result += str(count) + num
        return result
        