class Solution(object):
    def addBinary(self, a,b):
        n = max(len(a), len(b))

        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0
        result = []

        for i in range(n-1,-1,-1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                result.append('1')
            else:
                result.append('0')

            carry //= 2
        if carry == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)