import random 

def solution(A):
	l = 0
	r = len(A)-1
	RndQuicksor(A,l,r)
	return A

def Partition(A, l, r):
	pivot_element = A[r]
	i = l

	for j in range(l,r):
		if A[j] <= pivot_element:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[i], A[r] = A[r], A[i]
	return i

def RndPartition(A, l, r):
	rand = random.randint(l,r)
	A[r], A[rand] = A[rand], A[r]
	return Partition(A, l, r)

def RndQuicksor(A, l, r):
	if l < r:
		p = RndPartition(A, l, r)
		RndQuicksor(A, l, p-1)
		RndQuicksor(A, p+1, r)