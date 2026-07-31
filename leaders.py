class Solution:
    def leaders(self, arr):
        n=len(arr)
        maxi=arr[n-1]
        ans=[maxi]
        for i in range(n-2,-1,-1):
            if arr[i]>=maxi:
                maxi=arr[i]
                ans.append(arr[i])
        ans.reverse()
        return ans
