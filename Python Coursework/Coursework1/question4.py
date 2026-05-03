# num = 345
# count=0
# while num > 0:
#     digit = num % 10
#     count+=1
#     num //= 10  # This results in 5, then 4, then 3
# print(count)

def count_digit(num):
    count=0
    while num>0:
        digit= num%10     # This gives the last digit of the number
        count+=1          # Increment the count for each digit found
        num//=10          # This removes the last digit from the number, effectively shifting all digits to the right
    print(count)
count_digit(75869)
count_digit(654)