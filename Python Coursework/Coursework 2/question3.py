def pair_sum(nums,k):
    count=0
    hm={}
    for i in range(0, len(nums)):
        x=nums[i]
        complement=k-x
        if complement in hm:
            count+=hm[complement]
        hm[x] = hm.get(x, 0) + 1
    return count

arr1=[1,5,7,-1]
print(pair_sum(arr1,6))
arr2=[1,5,7,-1,5]
print(pair_sum(arr2,6))