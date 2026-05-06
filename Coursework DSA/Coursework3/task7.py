class Solution:
    def countConsistentStrings(self, allowed, words):
        
        allowed_set = set(allowed)
        
        count = 0
        
        # Check each word
        for word in words:
            is_valid = True
            
            for ch in word:
                if ch not in allowed_set:
                    is_valid = False
                    break
            
            if is_valid:
                count += 1
        
        return count


# -------- USER INPUT --------
if __name__ == "__main__":
    sol = Solution()
    
    allowed = input("Enter allowed characters: ")
    
    n = int(input("Enter number of words: "))
    
    words = []
    print("Enter words:")
    for _ in range(n):
        words.append(input())
    
    result = sol.countConsistentStrings(allowed, words)
    
    print("Output:", result)