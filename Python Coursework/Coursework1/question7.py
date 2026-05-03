# list=[10, 20, 30 ,40 , 50 ,60]
# l=[]
# for i, x in enumerate(list):
#     if i%2!=0:
#         l.append(x)
# print(l)  

def odd_index(list):
    odd_l=[]     
    for i, x in enumerate(list):
        if i%2!=0:
            odd_l.append(x)  #append the element x to the odd_l list if its index i is odd 
    print(odd_l)
    
list1=10, 20, 30, 40, 50, 60, 70, 80, 90, 100
odd_index(list1)

list2=23, 46, 69, 92, 115
odd_index(list2)