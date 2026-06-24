arr = [10, 15, 20, 25, 30, 35, 40]
key = 35
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print("Element", key, "found at position", i + 1)
        found = True
        break
if not found:
    print("Element not found")