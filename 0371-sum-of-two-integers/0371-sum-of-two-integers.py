class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return self.add(a, b)


    def add(self, a, b):
        carry = (a & b) << 1  # 올림 수 저장
        result = a ^ b  # xor 연산으로 더함

        if carry != 0:
            return add(carry, result)
        else:
            return result
        
        



    