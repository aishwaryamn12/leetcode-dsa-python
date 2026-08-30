def findLargest(arr):
    maxi = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]

    return maxi


arr = [3, 7, 2, 9, 5]
print(findLargest(arr))
