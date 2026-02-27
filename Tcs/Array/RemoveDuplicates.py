Id = list(map(int,input().split()))

size = len(Id)

#Maintain order
#print(list(dict.fromkeys(Id)))

seen = set()
result=[]
for num in Id:
    if num not in seen :
        seen.add(num)
        result.append(num)

print(result)