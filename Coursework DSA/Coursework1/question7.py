def successfulPairs(spells, potions, success):

    potions.sort()
    
    m = len(potions)
    result = []
    
    for spell in spells:

        required = (success + spell - 1) // spell   # ceiling division

        left = 0
        right = m - 1
        index = m   
        
        while left <= right:
            mid = (left + right) // 2
            
            if potions[mid] >= required:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        
        result.append(m - index)
    
    return result

spells1 = [5,1,3]
potions1 = [1,2,3,4,5]
success1 = 7

print(successfulPairs(spells1, potions1, success1))

spells2=[3,1,2]
potions2=[8,5,8]
success2=16

print(successfulPairs(spells2, potions2, success2))