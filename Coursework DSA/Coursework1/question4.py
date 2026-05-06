def trap(arr):
    
    if len(arr)<3:
        return 0
    

    left = 0
    right = len(arr) - 1
    
    left_max = 0
    right_max = 0
    
    total_water = 0
    
    while left < right:
        
        if arr[left]<arr[right]:
            if arr[left]>=left_max:
                left_max=arr[left]
            else:
                trapped_water=left_max-arr[left]
                total_water+=trapped_water
            left+=1
        
        else:
            if arr[right]>=right_max:
                right_max=arr[right]
            else:
                trapped_water=right_max-arr[right]
                total_water+=trapped_water
            right-=1
    
    return total_water

arr1=[0,2, 0, 2,0]
print(trap(arr1))

arr2=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0]
print(trap(arr2))