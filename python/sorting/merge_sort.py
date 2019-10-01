def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        left_idx = right_idx = curr_idx = 0

        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] < right_arr[right_idx]:
                arr[curr_idx] = left_arr[left_idx]
                left_idx += 1
            else:
                arr[curr_idx] = right_arr[right_idx]
                right_idx += 1
            curr_idx += 1


        while left_idx < len(left_arr):
            arr[curr_idx] = left_arr[left_idx]
            left_idx += 1
            curr_idx += 1

        while right_idx < len(right_arr):
            arr[curr_idx] = right_arr[right_idx]
            right_idx += 1
            curr_idx += 1


arr = [5,4,3,1,2,3,1,1,3]
print('before', arr)
merge_sort(arr)
print('after', arr)

