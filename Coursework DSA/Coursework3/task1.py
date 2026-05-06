class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i]=left_product
            left_product*=nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i]*=right_product
            right_product*=nums[i]
        
        return answer

if __name__ == "__main__":
    sol = Solution()
    
    n = int(input("Enter number of elements: "))
    
    print("Enter the elements:")
    nums = list(map(int, input().split()))
    
    result = sol.productExceptSelf(nums)
    
    print("Output:", result)