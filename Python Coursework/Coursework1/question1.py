# l=[]
# n=int(input("Enter a non-negavtive integer: "))
# for i in range(0,n):
#     l.append(i**2)
# print(l)



def square(n):
    square_list=[]       #list that will store the squares of numbers from 0 to n-1
    for num in range(0,n):
        square_list.append(num**2)      #append the square of num to the list
    return square_list

print(square(5))
print(square(4))