A = [1,2,3,4,5]

for i in range(len(A)-2):
    if i%2 == 0:
        A[i], A[i+1] = A[i+1], A[i]



print(A)