def chocolate(arr,m):
    n=len(arr)+1    #number of chocolates in packet
    if m>n:
        return 0
    else:
        arr.sort()
        minimum_difference=float('inf')
        for i in range(0, n-m):
            difference= arr[i+m-1]-arr[i]
            if difference<minimum_difference:
                minimum_difference=difference
    return minimum_difference

arr1=[7, 3, 2, 4, 9, 12, 56]
print(chocolate(arr1,3))

arr2=[3, 4, 1, 9, 56, 7, 9, 12]
print(chocolate(arr2,5))
