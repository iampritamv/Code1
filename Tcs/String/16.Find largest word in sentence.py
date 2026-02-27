s = input()

words = s.split()

largest =""

for w in words :
    if len(w) > len(largest) :
        largest = w
print(largest)