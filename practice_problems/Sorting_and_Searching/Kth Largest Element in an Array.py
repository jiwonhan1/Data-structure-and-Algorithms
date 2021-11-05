import heapq
import random
class Solution(object):
    # Time complexity O(N log k) Space complexity O(K)
    def findKthLargest(self, nums,k):
        return heapq.nlargest(k, nums)[-1]

    # Quickselect
    # Time complexity O(N) in the average case, O(N2) in the worse case
    # Space complexity O(1)
    def findKthLargest2(self, nums,k):
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
                nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index-1, k_smallest)
            else:
                return select(pivot_index+1, right, k_smallest)
        return select(0, len(nums)-1, len(nums) - k)