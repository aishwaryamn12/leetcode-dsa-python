class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        colms=len(matrix[0])
        zero_rows=set()
        zero_colms=set()
        for i in range(rows):
            for j in range(colms):
                if matrix[i][j]==0:
                    zero_rows.add(i)
                    zero_colms.add(j)
        for i in range(rows):
            for j in range(colms):
                if i in zero_rows or j in zero_colms:
                    matrix[i][j]=0            
