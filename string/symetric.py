
# def solve(txt):
#     size=len(txt)
    
#     half=size//2
    
#     j=half

#     if size % 2 != 0: 
#         print("Not symmetrical")

#     for i in range(0 , half):

#         if(txt[i]!=txt[j]):
#             print("Not symmetrical")
#             return
#         else:
#             i+=1
#             j+=1
#     print("Symmetrical")    

def symmetrical(txt):
    size = len(txt)

    half = size//2

    if size%2 == 0 :
        return txt[:half] == txt[half:]
    
    else:
        return txt[:half] == txt[half+1:]

txt = input("Enter the string \n")

if symmetrical(txt):
    print("Symmetrical")
else:
    print("Not Symmetrical")