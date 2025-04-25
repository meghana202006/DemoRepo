def partition(arr , s , e):

	pivot = e

	i = s - 1

	for j in range(s , e):

		if(arr[j] <= arr[pivot]):

			i += 1

			arr[i] , arr[j] = arr[j] , arr[i]

	arr[i + 1] , arr[pivot] = arr[pivot] , arr[i + 1]

	return i + 1

def quickSort(arr , s , e):

	if(s < e):

		pi = partition(arr , s , e)

		quickSort(arr , s , pi-1)

		quickSort(arr , pi+1 , e)

arr = [9 , 3 , 4 , 6 , 8 , 2 , 1 , 7 , 5]

print("Array before sorting:")
print(arr)

quickSort(arr , 0 , len(arr)-1)

print("Array after sorting:")
print(arr)