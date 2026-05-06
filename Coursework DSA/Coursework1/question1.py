def longestSubarraySumK(arr, k):
    
    prefix_sum = 0
    max_length = 0
    prefix_map = {} 
    
    for i in range(len(arr)):

        prefix_sum += arr[i]

        if prefix_sum == k:
            max_length = i + 1
        
        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_length = max(max_length, length)

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    
    return max_length


arr1 = [10, 5, 2, 7, 1, -10]
print(longestSubarraySumK(arr1, 15))

arr2=[-5, 8, -14, 2, 4, 12]
print(longestSubarraySumK(arr2, -5))

arr3=[10, -10, 20, 30]
print(longestSubarraySumK(arr3, 5))