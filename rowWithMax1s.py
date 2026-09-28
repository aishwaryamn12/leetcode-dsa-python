class Solution:
    def rowWithMax1s(self, mat):
        n=len(mat)
        m=len(mat[0])
        row=0
        col=m-1
        ans=-1
        while row<n & col>=1:
            if mat[row][col]==1:
                ans=row
                col-=1
            else:
                row+=1
        return ans           
       
