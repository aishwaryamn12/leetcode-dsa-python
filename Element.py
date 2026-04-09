arr = [5, 10, 15, 20, 25]
target = 15

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
