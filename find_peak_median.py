class Solution:
    def findMedian(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        l = min(row[0] for row in matrix)
        r = max(row[-1] for row in matrix)

        while l <= r:
            mid = (l + r) // 2
            count = 0

            for row in matrix:
                for num in row:
                    if num <= mid:
                        count += 1

            if count <= (rows * cols) // 2:
                l = mid + 1
            else:
                r = mid - 1

        return l
