from collections import Counter
import heapq
import random
class Solution:
    # Approach : Heap
    # Time complexity O(NlogK) if k < n and O(N) in the particular case of N=k
    # Space complexity O(N+k)
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), k=count.get)

    # Approach : Quickselect

    def topKFrequent2(self, nums,k):
        count = Counter(nums)
        unique= list(count.keys())

        def partition(left, right, pivot_index):
            pivot_freq = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest):
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index -1, k_smallest)
            else:
                quickselect(pivot_index+1, right, k_smallest)

        n = len(nums)
        quickselect(0, n-1, n-k)
        return unique[n-k:]
