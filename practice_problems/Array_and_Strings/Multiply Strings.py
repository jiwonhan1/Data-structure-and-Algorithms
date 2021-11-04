class Solution(object):
    # Time complexity O(MN) Space complexity O(M+N)
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        N = len(num1) + len(num2)
        answer = [0] * N

        # reverse the sequence for num1 and num2
        first_number = num1[::-1]
        second_number = num2[::-1]

        for place2, digit2 in enumerate(second_number):
            for place1, digit1 in enumerate(first_number):
                nums_zeros = place1 + place2
                carry = answer[nums_zeros]

                muptiplication = int(num1[digit1]) * int(num2[digit2]) + carry

                answer[nums_zeros] = muptiplication % 10

                answer[nums_zeros + 1] += muptiplication // 10
        if answer[-1] == 0:
            answer.pop()
        return ''.join(str(digit) for digit in reversed(answer))

