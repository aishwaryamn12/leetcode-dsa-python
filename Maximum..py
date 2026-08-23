arr = [10, 25, 7, 40, 15]

maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print(maximum)
