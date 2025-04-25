def calc(A,B):
    nums = [0]*4*10**6
    for i in range(len(A)):
        nums[A[i]] += 1
    ans = []
    for i in range(len(B)):
        if nums[i] <= B[i]:
            ans.append('1')
        else:
            ans.append('0')
    return "".join(ans)