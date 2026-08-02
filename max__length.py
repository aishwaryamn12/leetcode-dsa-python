class Solution:
    def maxLength(self, arr):
        max_length=0
        prefix_map={}
        prefix_sum=0
        n=len(arr)
        for i in range(n):
            prefix_sum+=arr[i]
            if prefix_sum==0:
                max_length=i+1
            elif prefix_sum in prefix_map:
                length=i-prefix_map[prefix_sum]
                max_length=max(max_length,length)
            else:
                prefix_map[prefix_sum]=i
        return max_length        
        
