def binary_search(arr,L,R,x):
    if R>=L:
        mid=L+(R-1)//2
        if arr[mid]==x:
             return mid
        elif arr[mid]>x:
            return binary_search(arr,L,mid-1,x)
        else:
            return binary_search(arr,mid+1,R,x)
    else:
        return -1

arr =[0,2,3,4,10,40,44]
x=40
result = binary_search(arr,0,len(arr)-1,x)
if result !=-1:
    print("Element is present at index "+str(result))
else:
    print("Element is not present in array")