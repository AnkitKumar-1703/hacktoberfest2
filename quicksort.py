def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Choose a pivot element
    pivot = arr[len(arr) // 2]
    
    # Partitioning step
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply quicksort on partitions
    return quicksort(left) + middle + quicksort(right)
