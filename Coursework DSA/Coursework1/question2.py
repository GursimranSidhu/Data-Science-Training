def maxProductTriplet(arr):
    
    n=len(arr)
    if n < 3:
        return 0
        
    else:
        arr.sort()
        
        product1= arr[n-3]*arr[n-2]*arr[n-1]
        product2=arr[0]*arr[1]*arr[n-1]
        
        max_product=max(product1, product2)
        
    if product1<=product2:
        return [arr[0],arr[1],arr[n-1]]
    
    if product1>product2:
        return arr[n-3],arr[n-2],arr[n-1]

    
arr1=[ -4, 1, -8, 9, 6]
print(maxProductTriplet(arr1))

arr2=[1, 7, 2, -2, 5]
print(maxProductTriplet(arr2))