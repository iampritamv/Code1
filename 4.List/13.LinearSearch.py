def linear_search(arr, target):
    for i in range(0 , len(arr)):
        if arr[i]==key :    
            return i 
    return -1



arr=[1,23,4,5,5,34,234,5,34,]
key = 34

result = linear_search(arr,key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")