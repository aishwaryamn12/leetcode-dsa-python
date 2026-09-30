class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        l = 0
        r = cols - 1

        while l <= r:
            mid = (l + r) // 2

            max_row = 0

            for i in range(rows):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            left = mat[max_row][mid - 1] if mid > 0 else -1
            right = mat[max_row][mid + 1] if mid < cols - 1 else -1

            if mat[max_row][mid] > left and mat[max_row][mid] > right:
                return [max_row, mid]

            elif right > mat[max_row][mid]:
                l = mid + 1

            else:
                r = mid - 1
