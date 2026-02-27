# list = [ 1 , 2 ,3 ,4 ,5 ,6]
# print(len(list))


def sum(list):
    sum = 0
    for i in range(0 , len(list)):
        sum = sum + list[i]

    return sum 

list = [ 1 , 2 ,3 ,4 ,5 ,6]
print(sum(list))