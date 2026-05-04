def rearrange_negatives(arr):
    n = len(arr)

    for i in range(1, n):

        if arr[i]<0:
            temp=arr[i]
            j=i-1
            while j>=0 and arr[j]>0:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=temp

    return arr

arr1= [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(rearrange_negatives(arr1))
arr2=[-12, 11, 13, -5, 6, -7, 5, -3, 8]
print(rearrange_negatives(arr2))