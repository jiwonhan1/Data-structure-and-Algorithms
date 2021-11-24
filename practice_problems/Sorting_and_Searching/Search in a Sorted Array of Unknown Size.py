class ArrayReader:
    def get(self, index)

class Solution:
    # Time complexity O(logT)
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0

        left, right = 0,1

        while reader.get(right) < target:
            left = right
            right += 1

        while left <= right:
            pivot = left + (right-left) // 2
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot -1
            else:
                left = pivot + 1
        return -1