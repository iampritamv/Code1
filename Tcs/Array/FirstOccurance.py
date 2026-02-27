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