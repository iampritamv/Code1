# def BinaryS(arr , key):

#     start = 0 
#     end = len(arr) - 1
#     mid = start + (end - start)//2

#     while start <= end :

#         if arr[mid] == key :
#             return mid
        
#         if arr[mid] < key :
#             start = mid + 1
        
#         else :
#             end = mid - 1
        
#         mid = start + (end - start)//2

# for 1st occurance
def BinaryS(arr , key):

    start = 0 
    end = len(arr) - 1
    mid = start + (end - start)//2
    result = -1

    while start <= end :

        if arr[mid] == key :
            result = mid
            end = mid - 1
        
        if arr[mid] < key :
            start = mid + 1
        
        else :
            end = mid - 1
        
        mid = start + (end - start)//2

key = 3  
arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]

print(BinaryS(arr , key))

