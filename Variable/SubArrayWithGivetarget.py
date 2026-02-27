arr = list(map(int , input().split(','))) #9 4 20 3 10 5
target = int(input("Enter target "))
size = len(arr) #6
for i in range(0 , size):

    sum = 0 

    for j in range(i , size):

        sum += arr[j] 

        if(sum == target):
            print(*arr[i : j + 1])