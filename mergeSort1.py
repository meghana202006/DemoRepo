def merge(arr , l , m , r):

	i = l 
	j = m + 1

	temp = []

	while(i <= m and j <= r):

		if(arr[i] <= arr[j]):

			temp.append(arr[i])

			i += 1

		elif(arr[j] <= arr[i]):

			temp.append(arr[j])

			j += 1

		
	while(i <= m):

		temp.append(arr[i])

		i += 1

	while(j <= m):

		temp.append(arr[j])
		
		j += 1


	startOfList = l

	startOftemp = 0

	while(startOftemp < len(temp)):
		
		arr[startOfList] = temp[startOftemp]

		startOfList += 1

		startOftemp += 1


def mergeSort(arr , l , r):

	if(l < r):

		m = (l + r)//2

		mergeSort(arr , l , m)

		mergeSort(arr , m + 1 , r)

		merge(arr , l , m , r)


arr = [6 , 4 , 2 , 3 , 9 , 8 , 5 , 1]

print("Array before sorting:")
print(arr)

mergeSort(arr , 0 , len(arr)-1)

print("Array after sorting:")
print(arr)


		
