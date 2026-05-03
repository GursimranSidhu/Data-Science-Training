# n=int(input("Enter a number:"))
# sum=0
# term=0
# for i in range(0,n):
#     term=term*10+2
#     sum=term+sum
# print(sum)

def sumseries(n):
    sum=0
    term=0
    for i in range(0,n):
        term=term*10+2    
        sum=sum+term      
    print(sum)

sumseries(5)
sumseries(6)