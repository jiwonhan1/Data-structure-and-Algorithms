class Solution:
    # Down Top method
    # Time complexity O(NlogN)
    def sortArray(self, nums):
        if len(nums) >1:
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            self.sortArray(left_half)
            self.sortArray(right_half)

            i,k,j = 0, 0, 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

            while j < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1
        return nums



# Top Down method
# Time complexity O(N)
def merge_sort(nums):
    # bottom cases: empty or list of a single element
    if len(nums) <=1:
        return nums
    pivot = int(len(nums) /2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)

def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])
    return ret