# n = int(input())
# arr = list(map(int , input().split()))
# print("array ", *arr[:n])
# # print(arr)

arr = list(map(int, input().split()))
print(arr)

def input_array():
    arr = []
    while True:
        line = input()
        if not line:
            break
        arr += list(map(int, line.split()))
    return arr