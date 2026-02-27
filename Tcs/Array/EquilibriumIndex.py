n = list(map(int , input().split()))
total = sum(n)

left = 0

for i in range(len(n)):
    right = total - left - n[i]

    if left == right :
        print(i)
        break

    left = left + n[i]

else:
    print("No equilibrium")