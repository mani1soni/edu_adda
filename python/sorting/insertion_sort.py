def insertion_sort(arr):
    size = len(arr)
    for i in range(1,size):
        value = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > value:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = value


arr = [5,4,3,1,2,3,1,1,3]
print('before', arr)
insertion_sort(arr)
print('after', arr)

