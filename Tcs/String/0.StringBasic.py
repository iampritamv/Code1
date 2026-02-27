
#1. String slicing
# s = "Python"

# print(s[0:4])   # Pyth
# print(s[:3])    # Pyt
# print(s[2:])    # thon
# print(s[::-1])  # nohtyP (reverse string)

#2. Loop through string
# s = "Code"

# for ch in s:
#     print(ch)

#3 . Convert case
s = "python"

print(s.upper())   # PYTHON
print(s.lower())   # python
print(s.capitalize()) # Python

#4 . Remove spaces

s = "  hello  "

print(s.strip())   # "hello"

#5. Replace characters

s = "I like Java"

print(s.replace("Java","Python"))

#6. Check substring

s = "Python programming"

print("Python" in s)   # True
print("Java" in s)     # False

#7 . Count characters

s = "banana"

print(s.count('a'))   # 3

#9 . Find position
s = "Python"

print(s.find('t'))