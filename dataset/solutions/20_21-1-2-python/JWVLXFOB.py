def solution(A):
    divide(A, 0, len(A)-1)
    return A
    
def divide(A, start, end):
    if start >= end:
        return

    mid = (start + end)//2
    divide(A, start, mid)
    divide(A, mid + 1, end)
    merge(A, start, end, mid)
    
def merge(A, start, end, mid):
    left = A[start:mid + 1]
    right = A[mid+1:end+1]

    left_index = 0
    right_index = 0
    A_index = start

    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            A[A_index] = left[left_index]
            left_index = left_index + 1
        else:
            A[A_index] = right[right_index]
            right_index = right_index + 1

        A_index = A_index + 1

    while left_index < len(left):
        A[A_index] = left[left_index]
        left_index = left_index + 1
        A_index = A_index + 1

    while right_index < len(right):
        A[A_index] = right[right_index]
        right_index = right_index + 1
        A_index = A_index + 1