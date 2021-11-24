from collections import defaultdict
class Solution:
    # Time and space complexity O(l1 * l2 * x)
    # x refers to average string length
    def findRestaurant(self, list1, list2):
        mapping = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j not in mapping:
                        mapping[i+j] = []
                    mapping[i+j].append(list1[i])

        min_index_sum = float('inf')
        for key in mapping.keys():
            min_index_sum = min(min_index_sum, key)

        return mapping.get(min_index_sum)

    def findRestaurant2(self, list1, list2):
        mapping = defaultdict(list)

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    mapping[i+j].append(list1[i])

        min_index = float('inf')
        for key in mapping.keys():
            min_index = min(min_index, key)

        return mapping.get(min_index)