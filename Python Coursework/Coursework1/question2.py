# string=input("Enter any string: ")
# result=""
# for char in string:
#     if char not in result:
#         result+=char
# print(result)

def unique_element(s):
    result=""   
    for char in s:
        if char not in result:
            result+=char        #append the unique character to the result string
    print("Unique elements in the list are: ",result)
unique_element("abaabbbacd")
unique_element("ddeefggh")