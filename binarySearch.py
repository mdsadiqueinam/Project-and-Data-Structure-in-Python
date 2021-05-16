import numpy as np
try :
    arr = list(map(int, input("Enter the space seprated inegers\n").strip().split()))
    x = int(input("enter the value to search:   "))
    arr = np.array(sorted(arr), int)
    l, r, mid = 0, len(arr)-1, (len(arr)-1)//2
    while(l<=r) :
        if arr[mid]==x :
            break;
        elif arr[mid]>x : r = mid-1
        else : l = mid+1
        mid = (l+r)//2
    if arr[mid]==x : print("Value found at index", mid)
    else : print("Value not in array")

except :
    print("Invalid input please enter the integers val only")