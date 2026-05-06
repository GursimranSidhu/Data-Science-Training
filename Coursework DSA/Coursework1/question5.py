def nextPermutation(nums):
    
    n = len(nums)

    if n <= 1:
        return

    pivot = -1
    
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
 
    if pivot != -1:
        
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                swap_index = j
                break
        nums[pivot], nums[swap_index] = nums[swap_index], nums[pivot]
    
    
    left = pivot + 1
    right = n - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums
        
num1=[1,2,3]
print(nextPermutation(num1))

num2=[3,2,1]
print(nextPermutation(num2))

num3=[1,1,5]
print(nextPermutation(num3))