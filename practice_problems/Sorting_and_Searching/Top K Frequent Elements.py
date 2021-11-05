from collections import Counter
import heapq
import random

class Solution:
    def topKFrequent(self, nums,k):
        if k == len(nums):
            return nums
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2. build heap of top k frequent elements and convert it into an output array
        # O(N log K) time
        return heapq.nlargest(k, count.keys(), key=count.get)

    # Time complexity O(N) in average case, O(N2) in the worst case
    # Space complexity O(N)
    def topKFrequest2(self, nums,k):
        count = Counter(nums)
        unique = list(nums.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[pivot_index]

            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[left]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest):
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left,right,pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index-1, k_smallest)
            else:
                quickselect(pivot_index+1, right, k_smallest)

        n = len(unique)
        quickselect(0, n -1, n -k)
        return unique[n-k:]