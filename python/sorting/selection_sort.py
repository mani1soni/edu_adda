def selection_sort(arr):
	for i in range(len(arr)):
		min_index = i;  # Index of minimal element 
		for j in range (i+1, len(arr)):  # Lookig for the minimal element in the unsorted part
			if (arr[min_index] > arr[j]):
				min_index = j

		if not i == min_index:  # swapping if needed
			arr[i], arr[min_index] = arr[min_index], arr[i]  # swapping

test_list = [2, 4, 6, 4, 12, 5]
print("before:", test_list)
selection_sort(test_list)
print("after:", test_list)