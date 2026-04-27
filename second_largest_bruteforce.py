arr=[7,3,2,5,0]
largest=arr[0]
n=len(arr)
for i in range(n):#len(arr)
    if arr[i]>largest:
        largest=arr[i]
    second=-1
for i in range(n):
    if arr[i]!=largest and arr[i]>second:
        second=arr[i]        
print(second)
