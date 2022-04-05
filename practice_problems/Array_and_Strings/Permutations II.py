class Solution:
    def permuteUnique(self, nums):
        result = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                result.append(list(comb))
                return
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    print(comb)
                    comb.pop()
                    counter[num] += 1
            backtrack([], Counter(nums))
            return result
