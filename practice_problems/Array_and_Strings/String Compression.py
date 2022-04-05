class Solution:
    def compress(self, chars):
        answer = ""
        count = 0
        length = len(chars)

        chars_copy = chars

        while chars_copy:
            count = 0
            current = chars_copy[0]

            for i in range(0,len(chars_copy)-1):
                if chars_copy[i] == chars_copy[i+1]:
                    count += 1
                else:
                    break
            if count > 0:
                answer += current+str(count)
            if count == 0:
                answer += current
            chars_copy = chars_copy[count+1:]
        chars += answer
        del chars[0:length]