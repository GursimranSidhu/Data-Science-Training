# n1=int(input("Enter the number: "))
# fact=1
# for i in range(1, n1+1):
#     fact=fact*i
# print(fact)

def factorial(n):
    fact=1    
    for i in range(1, n+1):
        fact=fact*i   
    print(fact)

factorial(4)
factorial(2)