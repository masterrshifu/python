A = [1,2,3,4,5,6]

print(A)

N = len(A)

B = 2


start = 0
end = N-1

while(start < end):
    A[start], A[end] = A[end], A[start]
    start = start+1
    end = end-1


print(A)


start = 0
end = B-1

while(start < end):
    A[start], A[end] = A[end], A[start]
    start = start+1
    end = end-1

print(A)

start = B
end = N-1

while(start < end):
    A[start], A[end] = A[end], A[start]
    start = start+1
    end = end-1

print(A)




