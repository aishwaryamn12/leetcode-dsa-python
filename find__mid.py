class Solutions:
    def find_mid(self,matrix):
        rows=len(matrix)

        columns=len(matrix[0])
        l=min(row[0] for row in matrix)
        r=max(row[-1] for row in matrix)
        while l<=r:
            mid=(l+r)//2
            count=0
            for row in matrix:
                for num in row:
                    if num<=mid:
                        count+=1
            if count<=(rows*columns)//2:
                l=mid+1
            else:
                r=mid-1
        return l
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
obj=Solutions()
print(obj.find_mid(matrix))                        



