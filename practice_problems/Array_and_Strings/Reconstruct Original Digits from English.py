from collections import Counter
class Solution(object):
    # Time complexity O(N)
    # Space complexity O(1)
    def originDigits(self, s):

        count = Counter(s)

        out = {}

        out['0'] = count['z']
        out['2'] = count['w']
        out['4'] = count['u']
        out['6'] = count['x']
        out['8'] = count['g']
        out['3'] = count['h'] - count['8']
        out['5'] = count['f'] - out['4']
        out['7'] = count['s'] - out['6']
        out['9'] = count['i'] - out['5'] - out['6'] - out['8']
        out['1'] = count['n'] - out['7'] - 2 * count['9']

        output = [key * out[key] for key in sorted(count.keys())]

        return ''.join(output)