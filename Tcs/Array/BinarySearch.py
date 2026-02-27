arr = list(map(int , input().split()))
target = int(input())
start = 0 
end = len(arr) - 1
while start <= end :

    mid = (start+end )//2

    if arr[mid] == target :
        print(mid)
        break

    elif target > arr[mid]:
        start = mid+1

    else :
        end = mid - 1

else :
    print("Not Found")  