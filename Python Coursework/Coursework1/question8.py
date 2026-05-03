# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))

# if (a>b and b>c) or (a<b and b<c):
#     print("Output: ",b)
# elif (b>a and a>c) or (a>b and a<c):
#     print("Output: ", a)
# else:
#     print("Output: ", c)
    
    
def median_no(a, b, c):
    if (a>b and b>c) or (a<b and b<c):      
        print("Output: ",b)
    elif (b>a and a>c) or (a>b and a<c):     
        print("Output: ", a)
    else:                                  
        print("Output: ", c)

n1=int(input("Input first number: "))
n2=int(input("Input second number: "))
n3=int(input("Input third number: "))

median_no(n1,n2,n3)