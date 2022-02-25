class Solution(object):
    def replaceElements(self,arr):
        mx = -1
        for i in range(len(arr) -1, -1, -1):
            arr[i], mx = mx, max(arr[i], mx)
        return arr