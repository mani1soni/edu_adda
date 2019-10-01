 #!/usr/bin/env-python3

 # this code used to sort a given array (list) with bubble sort algorithm

def bubbleSort(arr):
	for passnum in range(len(arr)-1, 0, -1) :
		for i in range(passnum):
			if arr[i]>arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp


listSample = [5, 4, 2, 2, 1, 10, 12]

# call a function
bubbleSort(listSample)

# print a list
print(listSample)

