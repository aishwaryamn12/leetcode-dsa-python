class Solution:
    def kthElement(self, a, b, k):
        arr = a + b
        arr.sort()
        return arr[k - 1]
