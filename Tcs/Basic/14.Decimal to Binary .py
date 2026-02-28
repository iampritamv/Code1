n = int(input())

binary =""

if n == 0 :
    binary =='0'


while n > 0 :
    binary = str(n % 2)+binary
    n = n//2

print(binary)

# M - 2 
# n = int(input())
# print(bin(n)[2:])