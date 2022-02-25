class TwoSum(object):
    def __init__(self):
        self.nums = []
        self.is_sorted = False

    # Time complexity O(1)
    def add(self, number):
        self.nums.append(number)
        self.is_sorted = False

    # Time comlexity O(Nlog(N))
    def find(self, value):
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        low, high = 0, len(self.nums) -1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else:
                return True
        return False