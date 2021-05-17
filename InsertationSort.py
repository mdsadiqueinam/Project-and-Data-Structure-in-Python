import numpy as np

def insertionSort(arr) :
    for i in range(1,len(arr)) :
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key :
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def main() :
    try :
        arr = list(map(int, input("Enter the space seprated inegers\n").strip().split()))
        arr = np.array(sorted(arr), int)
        insertionSort(arr)
        print(arr)
    except :
        print("Invalid input please enter the integers val only")

if __name__=="__main__" :
    main()