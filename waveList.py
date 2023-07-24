A = [1,2,3,4,5,6,7,8]

N = len(A)

if N % 2 == 0:
    for i in range(N):
        if i % 2 == 0:
            A[i], A[i+1] = A[i+1], A[i]

else:
    for i in range(N-1):
        if i % 2 == 0:
            A[i], A[i+1] = A[i+1], A[i]

print(A)