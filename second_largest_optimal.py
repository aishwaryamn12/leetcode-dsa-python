arr=[5,3,6,6,7,9]
n=len(arr)
largest=-1
second=-1
for i in range(n):
    if arr[i]>largest:
        second=largest
        largest=arr[i]

    elif arr[i]!=largest and arr[i]>second:
        second=arr[i]
print(second)        
