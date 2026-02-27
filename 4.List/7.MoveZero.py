def pushZerosToEnd(arr):
	i = 0 
	for j in range(len(arr)):
		if arr[j] != 0 :
			arr[i],arr[j] = arr[j] , arr[i]
			i=i+1
	return arr
  

list1 = [3 , 5 , 0 , 0 ,4]
print(pushZerosToEnd(list1))