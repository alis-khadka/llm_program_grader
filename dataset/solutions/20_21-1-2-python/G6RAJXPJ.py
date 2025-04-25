import random

def solution(A):
    quick(A, 0, len(A) - 1)
    return A

def quick(arr, start , stop):
    if(start < stop):
        
        pivotindex = partitionrand(arr, start, stop)
         
        quick(arr , start , pivotindex-1)
        quick(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):
    
    randpivot = random.randrange(start, stop)
    
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    pivot = start 

    i = start + 1
 
    for j in range(start + 1, stop + 1):
     
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)