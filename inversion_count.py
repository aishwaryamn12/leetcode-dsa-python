class Solution:
    def merge(self, arr, l, mid, r):

        temp = []
        i = l
        j = mid + 1
        count=0
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count+=(mid-i+1)
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= r:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[l + k] = temp[k]
        return count

    def mergeSort(self, arr, l, r):

        if l >= r:
            return 0
        mid = (l + r) // 2
        count=0

        count+=self.mergeSort(arr, l, mid)
        count+=self.mergeSort(arr, mid + 1, r)
        count+=self.merge(arr, l, mid, r)
        return count
    def inversionCount(self,arr):
        return self.mergeSort(arr, 0, len(arr)-1)
        
        
