# list=[14,85,625,75]
# list1=[]
# for item in list:
#     if item>500:
#         break
#     elif item>150:
#         continue
#     elif item%5==0:
#         list1.append(item)
# print(list1)

def number_list(list):
    list1=[]                      
    for item in list:
        if item >500:   
            break                
        elif item>150:
            continue              
        elif item%5==0:
            list1.append(item)    
    print(list1)
list=[12,75,150,180,145,525,50]
number_list(list)    
list2=[14,85,625,75]  
number_list(list2) 