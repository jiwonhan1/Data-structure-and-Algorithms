class Solution:
    def fib(self, n):
        if n <= 1: return n
        one_back = 1
        two_back = 0
        for i in range(2, n+1):
            temp = one_back
            one_back += two_back
            two_back = temp
        return one_back