def nthFibonacci(n):
     
    if n <= 1:
        return n

    return nthFibonacci(n - 1) + nthFibonacci(n - 2)

n = int(input(" Enter a last term :  "))

print(nthFibonacci(n))