def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort_func(arr, low, high):
    if low < high:
        partition_idx = partition(arr, low, high)

        quick_sort_func(arr, low, partition_idx-1)
        quick_sort_func(arr, partition_idx+1, high)

def quick_sort(arr):
    quick_sort_func(arr, 0, len(arr)-1)


arr = [5,4,3,1,2,3,1,1,3]
print('before', arr)
quick_sort(arr)
print('after', arr)

