A = [-3,6,2,4,5,2,8,-9,3,1]

N = len(A)
B = []
B.append(A[0])

for i in range(1,N):
    val = max(B[i-1],A[i])
    B.append(val)


print(B)