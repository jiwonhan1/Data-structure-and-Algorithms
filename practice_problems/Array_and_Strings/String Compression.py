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

    def compress_string(self, string):
        compressed = []
        counter = 0

        for i in range(len(string)):
            if i != 0 and string[i] != string[i-1]:
                compressed.append(string[i-1] + str(counter))
                counter = 0
        counter += 1

        # add last repeated charater
        if counter:
            compressed.append(string[-1] + str(counter))
        return min(string, "".join(compressed), key = len)