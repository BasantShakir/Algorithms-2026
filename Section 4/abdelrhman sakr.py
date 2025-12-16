def selection_sort(arr):
    n = len(arr)
    
    print(f"Original array: {arr}\n")

    for i in range(n - 1):
        
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"Step {i + 1}: Swapped {arr[min_idx]} and {arr[i]} → {arr}")
        else:
            print(f"Step {i + 1}: {arr[i]} already in correct position → {arr}")
    
    return arr

array = [20, 19, 28, 56, 23, 45, 23, 65, 76, 43, 23, 45, 76, 23, 67]

sorted_array = selection_sort(array)

print(f"\nFinal sorted array: {sorted_array}")
print(f"\nTime Complexity: O(n²)")
print(f"Space Complexity: O(1)")