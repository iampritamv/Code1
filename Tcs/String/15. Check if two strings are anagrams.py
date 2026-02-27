# listen and silent → Anagram ✔
# hello and world → Not anagram ❌

# 👉 Two strings are anagrams if they 
# contain the same characters with same frequency, 
# order doesn’t matter.

s1=input().replace(" ","").lower()
s2=input().replace(" ","").lower()


if sorted(s1) == sorted(s2):
    print("Anagram")

else:
    print("Not Anagram")