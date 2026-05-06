class Solution:
    def removeDuplicates(self, s):
        stack = []
        
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)


# -------- USER INPUT --------
if __name__ == "__main__":
    sol = Solution()
    
    s = input("Enter string: ")
    
    result = sol.removeDuplicates(s)
    
    print("Output:", result)