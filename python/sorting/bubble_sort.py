def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [5,4,3,1,2,3,1,1,3]
print('before', arr)
bubble_sort(arr)
print('after', arr)
