# n=345
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)

def reverse_digit(n):
    rev=0
    while n>0:
        digit=n%10      
        rev=rev*10+digit    
        n//=10      
    print(rev)

reverse_digit(745633)
reverse_digit(65346)
    